from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey


from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    price = Column(DECIMAL(10, 2))
    retailer = Column(String(100))
