from operator import or_
from typing import List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from app import models, schemas

from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy.exc import NoResultFound
from app import models


def get_products(db: Session, search: str = None):
    if search:
        try:
            # Attempt to convert search term to float for price comparison
            price_search = float(search)
        except ValueError:
            price_search = None

        products = db.query(models.Product).filter(
            or_(
                models.Product.name == search,
                models.Product.price == price_search if price_search is not None else None,
                models.Product.retailer == search
            )
        ).all()

        if not products:
            raise NoResultFound(f"No Product found with search term '{search}'")
        return products

    return db.query(models.Product).all()


def create_products(db: Session, products: List[schemas.ProductCreate]):
    db_products = [models.Product(**product.model_dump()) for product in products]
    db.add_all(db_products)
    db.commit()
    for db_product in db_products:
        db.refresh(db_product)
    return db_products
#
