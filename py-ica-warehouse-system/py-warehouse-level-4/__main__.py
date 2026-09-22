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
            return []

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


    def get_products_by_price(self, min_price: int = 0, max_price: int = 0) -> list[str]:
        if min_price is None or min_price <= 0:
            return []
        if max_price is None or max_price <= 0:
            return []
        if max_price < min_price:
            return []

        products = []

        for product_id in self.products:
            price = self.products[product_id]["price"]

            if price >= min_price and price <= max_price:
                products.append(product_id)

        products.sort()

        return products


    def get_low_stock_products(self, threshold: int = 0) -> list[dict]:
        if threshold is None or threshold <= 0:
            return []
        else:
            low_stock = []

            for product_id in self.products:
                stock = self.products[product_id]["stock"]

                if stock <= threshold:
                    low_stock_details = {
                        "product_id": product_id,
                        "name": self.products[product_id]["name"],
                        "current_stock": self.products[product_id]["stock"],
                        "threshold": threshold
                    }
                    low_stock.append(low_stock_details)

            return low_stock


    def get_sales_by_date_range(self, start_timestamp: int = 0, end_timestamp: int = 0) -> list[dict]:
        if start_timestamp is None or start_timestamp < 0:
            return []
        if end_timestamp is None or end_timestamp < 0:
            return []
        if start_timestamp > end_timestamp:
            return []

        sales_timestamp = []

        for sale in self.sales:
            timestamp = sale["timestamp"]

            if timestamp >= start_timestamp and timestamp <= end_timestamp:
                sales_timestamp.append(sale)

        return sales_timestamp

    def sales_summary(self) -> dict:
        if len(self.products) == 0 or len(self.sales) == 0:
            return {
            "total_products": len(self.products),
            "total_units_sold": 0,
            "total_revenue": 0,
            "average_sale_size": 0,
            "products_in_stock": 0,
            "out_of_stock_products": len(self.products)
        }
        else:
            total_units_sold = 0
            products_in_stock = 0
            products_out_of_stock = 0

            for sale in self.sales:
                quantity = sale["quantity"]
                total_units_sold += quantity

            for product_id in self.products:
                stock = self.products[product_id]["stock"]
                if stock <= 0:
                    products_out_of_stock += 1
                else:
                    products_in_stock += stock

            average_sale_size = total_units_sold // len(self.sales)

            return {
            "total_products": len(self.products),              
            "total_units_sold": total_units_sold,           
            "total_revenue": self.total_revenue(),            
            "average_sale_size": average_sale_size,
            "products_in_stock": products_in_stock,          
            "out_of_stock_products": products_out_of_stock 
            }


    def restock_recommendation(self, min_threshold: int = 0) -> list[dict]:
        if min_threshold is None or min_threshold <= 0:
            return []
        else:
            restock = []
            recommendation = ""

            for product_id in self.products:
                stock = self.products[product_id]["stock"]
                total_sold = 0

                for sale in self.sales:
                    if sale["product_id"] == product_id:
                        total_sold += sale["quantity"]
  
                if stock <= 2:
                    recommendation = "URGENT"
                elif stock < min_threshold:
                    recommendation = "HIGH"
                else:
                    recommendation = "NORMAL" 

                restock_detail = {
                    "product_id": product_id,
                    "current_stock": stock,
                    "total_sold": total_sold,              
                    "recommendation": recommendation
                    }

                restock.append(restock_detail)

            return restock
     
    