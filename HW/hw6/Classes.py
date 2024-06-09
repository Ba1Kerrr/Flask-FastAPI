import datetime
from dataclasses import Field
from datetime import time
from typing import List

from pydantic import BaseModel, EmailStr


# Создание модели продукт
class Product(BaseModel):
    title: str
    description: EmailStr
    price: float


# Вставка в таблицу модели продукт
class ProductIn(Product):
    id: int


# Создание модели пользователя
class User(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str


# Вставка в таблицу пользователи
class UserIn(User):
    id: int


# Создание модели заказы
class Order(BaseModel):
    firstname: int
    lastname: int
    id_product: int
    data_order: str
    status_order: str

# Вставка в таблицу пользователи


class OrderIn(Order):
    id: int
