from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import select
from sqlalchemy import Table
Base = declarative_base()
engine = create_engine(r"sqlite:///C:\Users\student\Documents\Kosolapov\Project11\db.sqlite", echo = True)

associate_table = Table(
    "check_products",
    Base.metadata,
    Column("check_id", ForeignKey("check.id")),
    Column("product_id", ForeignKey("product.id"))
)

class Check(Base):
    __tablename__ = "check"
    id = Column(Integer, primary_key=True)
    time = Column(DateTime(), default = datetime.now)
    items = relationship("Product", secondary = associate_table)
    amount = Column(Integer, nullable = False)

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable = False)
    price = Column(Integer, nullable = False)
    barcode = Column(String(100), nullable = False)
    count = Column(Integer, nullable = False)
    guarantee = Column(Integer, nullable = False)

Base.metadata.create_all(engine)