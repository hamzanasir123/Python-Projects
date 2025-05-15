import json
from subClass import Electronics, Grocery, Clothing
from exceptions import DuplicateProductIDError, OutOfStockError, InvalidProductDataError

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.product_id in self._products:
            raise DuplicateProductIDError(f"Product ID {product.product_id} already exists.")
        self._products[product.product_id] = product

    def remove_product(self, product_id):
        self._products.pop(product_id, None)

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p.name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.__class__.__name__.lower() == product_type.lower()]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        product = self._products.get(product_id)
        if not product:
            raise KeyError("Product not found.")
        product.sell(quantity)

    def restock_product(self, product_id, quantity):
        product = self._products.get(product_id)
        if not product:
            raise KeyError("Product not found.")
        product.restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        expired_ids = [pid for pid, p in self._products.items()
                       if isinstance(p, Grocery) and p.is_expired()]
        for pid in expired_ids:
            del self._products[pid]

    def save_to_file(self, filename):
        data = [product.to_dict() for product in self._products.values()]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self._products.clear()
            for item in data:
                try:
                    ptype = item.get("type")
                    cls_map = {
                        "Electronics": Electronics,
                        "Grocery": Grocery,
                        "Clothing": Clothing
                    }
                    cls = cls_map.get(ptype)
                    if not cls:
                        raise InvalidProductDataError(f"Invalid product type: {ptype}")
                    product = cls.from_dict(item)
                    self.add_product(product)
                except Exception as e:
                    raise InvalidProductDataError(str(e))
