import csv
from sqlalchemy.orm import Session
from models import Base, Product, Order, OrderItem, InventoryItem
from database import engine, SessionLocal
import os

Base.metadata.create_all(bind=engine)

def load_csv(file_path, model, fieldnames):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        with SessionLocal() as session:
            for row in reader:
                obj = model(**{field: row[field] for field in fieldnames})
                session.add(obj)
            session.commit()

def main():
    load_csv("data/products.csv", Product, ["id", "name"])
    load_csv("data/orders.csv", Order, ["id", "status"])
    load_csv("data/order_items.csv", OrderItem, ["order_id", "product_id", "quantity"])
    load_csv("data/inventory_items.csv", InventoryItem, ["product_id", "quantity"])

if __name__ == "__main__":
    main()