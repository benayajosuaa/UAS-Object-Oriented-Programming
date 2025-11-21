# === LOGIC CRUD untuk PRODUCT ===

import json
from pathlib import Path
from src.models.product import Product

class ProductRepo:
    # load database
    def __init__(self, filepath="data/products.json"):
        self.filepath = Path(filepath)

    # FUNGSI CRUD Product
    # Get All
    def get_all(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    # Get by ID
    def find_by_id(self, product_id):
        data = self.get_all()
        for idproduct in data:
            if idproduct["id"] == product_id:
                return idproduct
        return None

    # Create
    def create(self, product: Product):
        Product.validate(product.to_database_json())

        data = self.get_all()

        if any(idproduct["id"] == product.id for idproduct in data):
            raise ValueError("ID produk sudah ada")

        data.append(product.to_database_json())

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return product.to_database_json()

    # Update
    def update(self, product_id, updates: dict):
        data = self.get_all()

        for idproduct in data:
            if idproduct["id"] == product_id:
                idproduct.update(updates)

                with open(self.filepath, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                return idproduct

        raise KeyError("Produk tidak ditemukan")

    # Delete
    def delete(self, product_id):
        data = self.get_all()

        new_data = [idproduct for idproduct in data if idproduct["id"] != product_id]

        if len(new_data) == len(data):
            raise KeyError("Produk tidak ditemukan")

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=2)

        return True
