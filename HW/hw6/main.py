from typing import List
import datetime

import databases
import sqlalchemy
from sqlalchemy import ForeignKey
from fastapi import FastAPI

from Classes import User, UserIn, Product, ProductIn, Order, OrderIn

app = FastAPI()
DATABASE_URL = "sqlite:///shop.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Создание таблица пользователи
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(30)),
    sqlalchemy.Column("lastname", sqlalchemy.String(30)),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
    sqlalchemy.Column("password", sqlalchemy.String(50))
)

# Создание таблицы заказы
orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", ForeignKey("users.firstname")),
    sqlalchemy.Column("lastname", ForeignKey("users.lastname")),
    sqlalchemy.Column("product_id", ForeignKey("products.id")),
    sqlalchemy.Column("order_date", sqlalchemy.Date()),
    sqlalchemy.Column("status", sqlalchemy.String(30))
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(30)),
    sqlalchemy.Column("description", sqlalchemy.String(50)),
    sqlalchemy.Column("price", sqlalchemy.Float)
)

# Подключение движка
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


# routing users
# Получить всех пользователей из бд
@app.get("/users/", response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


# Получить отдельного пользователя из бд
@app.get("/users/{user_id}", response_model=User)
async def get_users(users_id: int):
    query = users.select().where(users.c.id == users_id)
    return await database.fetch_one(query)


# Создать нового пользователя в бд
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


# Изменить пользователя в бд
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# Удалить пользователя из бд
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# routing orders
@app.get("/orders/", response_model=List[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


# Получить заказ из бд по id
@app.get("/orders/{order_id}", response_model=Order)
async def get_orders(orders_id: int):
    query = orders.select().where(orders.c.id == orders_id)
    return await database.fetch_one(query)


# Создать новый заказ в бд
@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


# Изменить заказ в бд
@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


# Удалить заказ из бд
@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'order deleted'}


# routing orders
# Создать новый продукт
@app.get("/products/", response_model=List[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


# Получить отдельный продукт из бд
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


# Создать нового продукта в бд
@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**products.dict())
    last_record_id = await database.execute(query)
    return {**products.dict(), "id": last_record_id}


# Изменить продукт в бд
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


# Удалить продукт из бд
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
