class Marketplace():

    def __init__(self):
        self.stores = {}
        self.products = {}
        self.sales = {}
        self.limits = {}

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
                if product["product_id"] == product_id:
                    product["stock"] -= quantity
                    new_sale = {
                        "product_id": product_id,
                        "quantity": quantity,
                        "timestamp": timestamp,
                        "remaining_stock": product["stock"]
                    }
                    self.sales[store_id].append(new_sale)

                    self.total_revenue += product["price"] * quantity
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


    def get_sales_history(self, store_id: str, limit: int) -> list[dict]:
        if store_id not in self.stores:
            return None
        else:
            sales_history = []

            for sale in self.sales[store_id]:
                product_price = 0

                for product in self.products[store_id]:
                    if product["product_id"] == sale["product_id"]:
                        product_price = product["price"]
                        break

                    past_sale = {
                        "product_id": sale["product_id"],
                        "quantity": sale["quantity"],
                        "timestamp": sale["timestamp"],
                        "revenue": sale["quantity"] * product_price
                    }
                    sales_history.append(past_sale)

            srt_sales_history = sorted(sales_history, key=lambda item: -item["timestamp"])
            return srt_sales_history[:limit]

    def top_products(self, store_id: str, n: int) -> list[tuple[str, int]]:
        if store_id not in self.stores:
            return None
        else:
            top_products = {}

            for sale in self.sales[store_id]:
                product_id = sale["product_id"]
                amount = sale["quantity"]

                if product_id not in top_products:
                    top_products[product_id] = amount
                else:
                    top_products[product_id] += amount

            srtd_products = sorted(top_products.items(), key=lambda item: -item[1])
            return srtd_products[:n]


    def daily_revenue(self, store_id: str, timestamp: int) -> int:
        if store_id not in self.stores:
            return None
        else:
            today_timestamp = timestamp // 1440
            daily_total = 0

            for sale in self.sales[store_id]:
                daily_timestamp = sale["timestamp"] // 1440

                if daily_timestamp == today_timestamp:
                    product_price = 0
                    for product in self.products[store_id]:
                        if product["product_id"] == sale["product_id"]:
                            product_price = product["price"]
                            break

                    daily_total += sale["quantity"] * product_price

            return daily_total

        
m = Marketplace()
print(m.create_store("amazon", 10))
print(m.add_product("amazon", "toothbrush", 2.99, 3))
print(m.get_store_info("amazon"))
print(m.add_product("amazon", "toothpaste", 4.99, 2))
print(m.make_sale("amazon", "toothbrush", 15, 1))
print(m.make_sale("amazon", "toothpaste", 20, 2))
print(m.get_store_info("amazon"))
print(m.get_sales_history("amazon", 5))
print(m.top_products("amazon", 2))
print(m.daily_revenue("amazon", 15))
