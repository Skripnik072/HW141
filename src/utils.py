import json
import os

from products import Product
from category import Category

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data_j = json.load(file)
    return data_j


def create_obj_from_json(data_j):
    category = []
    for cat in data_j:
        products = []
        for product in cat["products"]:
            products.append(Product(**product))
            print(product)
        cat["products"] = products
        category.append(Category(**cat))
        return category


if __name__ == "__main__":
    obj_data = read_json("date/products.json")
    class_data = create_obj_from_json(obj_data)
    print(class_data)

    print(class_data[0].name)
    print(class_data[0].products)