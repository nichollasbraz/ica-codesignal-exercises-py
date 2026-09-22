class Warehouse():

    def __init__(self):
        self.products = {}
        self.sales = []


    def create_product(self, product_id: str = "", name: str = "", price: int = 0) -> bool:
        if product_id is None or product_id == "":
            return False
        if name is None or name == "":
            return False
        if price is None or price <= 0:
            return False

        if product_id in self.products:
            return False
        else:
            self.products[product_id] = {
                "name": name,
                "price": price,
                "stock": 0
            }

            return True


    def add_stock(self, product_id: str = "", quantity: int = 0) -> bool:
        if product_id is None or product_id == "":
            return False
        if product_id not in self.products:
            return False

        if quantity is None or quantity <= 0:
            return False
        else:
            self.products[product_id]["stock"] += quantity
            return True

    def remove_stock(self, product_id: str = "", quantity: int = 0, timestamp: int = 0) -> int | None:
        if product_id is None or product_id == "":
            return None
        if product_id not in self.products:
            return None

        if quantity is None or quantity <= 0:
            return None
        elif quantity > self.products[product_id]["stock"]:
            return None
        else:
            self.products[product_id]["stock"] -= quantity

            new_sale = {
                "product_id": product_id,
                "quantity": quantity, 
                "timestamp": timestamp
            }

            self.sales.append(new_sale)

            return self.products[product_id]["stock"]


    def get_product_info(self, product_id: str = "") -> dict | None:
        if product_id is None or product_id == "":
            return None

        if product_id not in self.products:
            return None
        else:
            total_sold = 0

            for sale in self.sales:
                if sale["product_id"] == product_id:
                    total_sold += sale["quantity"]

            return {
                "product_id": product_id,
                "name": self.products[product_id]["name"],
                "price": self.products[product_id]["price"],
                "current_stock": self.products[product_id]["stock"],
                "total_sold": total_sold
            }

    