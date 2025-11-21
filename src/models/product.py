# buat class product
class Product : 
    def __init__(self, id, name, price, category, brand):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.brand = brand

    # ubah ke JSON untuk database
    def to_database_json (self):
        return {
            "id" : self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "brand": self.brand
        }

    # validasi data
    @staticmethod
    def validate(data):
        if not data.get("id"):
            raise ValueError("ID produk harus diisi")

        if not data.get("name") or not str(data["name"]).strip():
            raise ValueError("Nama produk harus diisi")

        if not isinstance(data.get("price"), int) or data["price"] < 0:
            raise ValueError("Harga harus berupa integer >= 0")

        if not data.get("category"):
            raise ValueError("Kategori produk harus diisi")

        if not data.get("brand"):
            raise ValueError("Brand produk harus diisi")