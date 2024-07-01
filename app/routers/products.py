from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, database

router = APIRouter(
    tags=["Products"]
)


@router.get("/products/", status_code=status.HTTP_200_OK)
def read_products(search: str = None, db: Session = Depends(database.get_db)):
    try:
        products = crud.get_products(db, search=search)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Products retrieved Successfully.",
                "success": True,
                "data": [
                    {
                        'id': product.id,
                        'name': product.name,
                        'price': float(product.price),
                        'retailer': product.retailer
                    }
                    for product in products
                ]
            }
        )
    except NoResultFound as ex:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": "Product does not exist.",
                "success": False,
                "error": str(ex)
            }
        )
    except Exception as ex:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Something Went Wrong.",
                "success": False,
                "error": str(ex),
            }
        )


@router.post("/products/", status_code=status.HTTP_201_CREATED)
def create_products(products: List[schemas.ProductCreate], db: Session = Depends(database.get_db)):
    try:
        response = crud.create_products(db, products)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Records created successfully.",
                "success": True,
                "data": [
                    {
                        'id': res.id,
                        'name': res.name,
                        'price': float(res.price),
                        'retailer': res.retailer
                    }
                    for res in response
                ]
            })
    except ValidationError as ex:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "message": "Invalid payload data.",
                "success": False,
                "error": str(ex)
            }
        )
    except Exception as ex:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Something went wrong.",
                "success": False,
                "error": str(ex)
            }
        )
