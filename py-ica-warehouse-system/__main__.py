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


    def get_sales_history(self, product_id: str = "") -> list[dict]:
        if product_id is None or product_id == "":
            return None

        if product_id not in self.products:
            return self.sales

        total_sales = []

        for sale in self.sales:
            if sale["product_id"] == product_id:
                total_sales.append(sale)

        sorted_sales = sorted(total_sales, key=lambda item: -item["timestamp"])
            
        return sorted_sales


    def best_seller(self) -> str | None:
        if len(self.products) == 0:
            return None
        if len(self.sales) == 0:
            return None
        else:
            total_sales = {}

            for sale in self.sales:
                product_id = sale["product_id"]
                quantity = sale["quantity"]

                if product_id not in total_sales:
                    total_sales[product_id] = quantity
                else:
                    total_sales[product_id] += quantity

            best_product = max(total_sales, key=lambda p: total_sales[p])

        return best_product


    def total_revenue(self) -> int:
        if len(self.products) == 0 or len(self.sales) == 0:
            return 0
        else:
            total_amount = 0

            for sale in self.sales:
                product_id = sale["product_id"]
                quantity = sale["quantity"]
                price = self.products[product_id]["price"]

                total_amount += quantity * price

            return total_amount


p1 = Warehouse()
print(p1.create_product("Mouse", "Mouse Logitech", 25))
print(p1.create_product("Monitor", "Monitor Asus", 11))
print(p1.__dict__)
print(p1.add_stock("Mouse", 15))
print(p1.add_stock("Monitor", 41))
print(p1.__dict__)
print(p1.remove_stock("Mouse", 12, 11))
print(p1.remove_stock("Monitor", 6, 22))
print(p1.remove_stock("Mouse", 3, 15))
print(p1.get_product_info("Mouse"))
print(p1.get_sales_history("Mouse"))
print(p1.best_seller())
print(p1.total_revenue())
