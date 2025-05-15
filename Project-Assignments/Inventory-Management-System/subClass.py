from Product import Product
from datetime import datetime

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity, warranty_years, brand):
        super().__init__(product_id, name, price, quantity)
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        return f"[Electronics] {self._name} ({self.brand}) - ${self._price} x {self._quantity_in_stock} | Warranty: {self.warranty_years} years"

    def to_dict(self):
        return {
            "type": "Electronics",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "warranty_years": self.warranty_years,
            "brand": self.brand
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()

    def is_expired(self):
        return datetime.today().date() > self.expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return f"[Grocery] {self._name} - ${self._price} x {self._quantity_in_stock} | Expires on: {self.expiry_date} ({status})"

    def to_dict(self):
        return {
            "type": "Grocery",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d")
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class Clothing(Product):
    def __init__(self, product_id, name, price, quantity, size, material):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name} - ${self._price} x {self._quantity_in_stock} | Size: {self.size}, Material: {self.material}"

    def to_dict(self):
        return {
            "type": "Clothing",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "size": self.size,
            "material": self.material
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
