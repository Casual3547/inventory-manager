from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class User(UserMixin,db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    username: Mapped[str] = mapped_column(String(100),nullable=False)
    email: Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    password_hash: Mapped[str] = mapped_column(String(100),nullable=False)
    products: Mapped[list['Product']] = relationship(back_populates='user')

class Product(db.Model):
    __table_name = "product"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    selling_price: Mapped[float] = mapped_column(Float,nullable=False)
    stock: Mapped[float] = mapped_column(Float,nullable=False)
    description: Mapped[str] = mapped_column(String(100),nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="products")

