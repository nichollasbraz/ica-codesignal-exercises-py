class Marketplace():

    def __init__(self):
        self.stores = {}
        self.products = {}
        self.sales = {}

        self.total_revenue = 0
        self.total_products_sold = 0
        self.total_sales = 0
        self.total_products = 0


    def create_store(self, store_id: str, timestamp: int) -> bool:
        if store_id not in self.stores:
            self.stores[store_id] = timestamp
            self.products[store_id] = []
            self.sales[store_id] = []
            return True
        else:
            return False


    def add_product(self, store_id: str, product_id: str, price: int, stock: int) -> bool:
        if store_id not in self.stores:
            return False
        else:
            product_finder = False

            for product in self.products[store_id]:
                if product["product_id"] == product_id:
                    product["price"] = price
                    product["stock"] += stock
                    product_finder = True
                    break

            if not product_finder:
                new_product = {
                    "product_id": product_id,
                    "price": price,
                    "stock": stock
                }
                self.products[store_id].append(new_product)
                self.total_products += len(self.products)

            return True


    def make_sale(self, store_id: str, product_id: str, timestamp: int, quantity: int) -> int | None:
        if store_id not in self.stores:
            return None
        else:
            product_finder = False

            for product in self.products[store_id]:
                if product["stock"] < quantity:
                    return None
                elif product["product_id"] == product_id:
                    product["stock"] -= quantity
                    new_sale = {
                        "product_id": product_id,
                        "quantity": quantity,
                        "timestamp": timestamp,
                        "remaining_stock": product["stock"]
                    }
                    self.sales[store_id].append(new_sale)

                    self.total_revenue = product["price"] * quantity
                    self.total_products_sold += quantity
                    self.total_sales += 1

                    product_finder = True
                    return new_sale["remaining_stock"]

            if not product_finder:
                return None


    def get_store_info(self, store_id: str) -> dict | None:
        if store_id not in self.stores:
            return None
        else:
            return {
                "store_id": store_id,
                "total_revenue": self.total_revenue,          
                "total_products_sold": self.total_products_sold,      
                "total_sales": self.total_sales,              
                "total_products": self.total_products
            }


m = Marketplace()
print(m.create_store("amazon", 10))
print(m.add_product("amazon", "toothbrush", 2.99, 1))
print(m.get_store_info("amazon"))
print(m.add_product("amazon", "colgate", 4.99, 2))
print(m.products)
print(m.make_sale("amazon", "toothbrush", 15, 1))
print(m.sales)
print(m.get_store_info("amazon"))