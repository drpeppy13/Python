class Product(object):
    def __init__(self, price, item_name, weight, brand, status, return_status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.return_status = return_status
    def sell(self):
        self.status = "Sold"
        return self
    def display_info(self):
        print "price", self.price
        print "item_name", self.item_name
        print "weight", self.weight
        print "brand", self.brand
        print "status", self.status
        print "return_status", self.return_status
        return self
    def add_tax(self):
        sales_tax = self.price * 0.12
        total_price = self.price + sales_tax
        self.price = total_price
        return self
    def return_product(self):
        if self.return_status == "like new":
            self.status = "For Sale"
        elif self.return_status == "defective":
            self.status = "Defective" 
            self.price = 0
        elif self.return_status == "opened":
            self.status = "used" 
            used_price = self.price * 0.80 
            self.price = used_price 
        return self
          

product1 = Product(2, "Tomato", 2, "Costco", "For Sale", "like new")
product2 = Product(3, "Oranges", 2, "Dole", "For Sale", "defective")
product3 = Product(3, "Strawberries", 1, "Costco", "For Sale", "opened")
product4 = Product(2, "Cucumber", 3, "Ralphs", "For Sale", "like new")

# product1.sell()
# changes product 1 to sold status
# 
# product1.display_info()
# display info of product 1
# 
# chain commands 
# add tax + display info
# product1.add_tax().display_info()

#return product
#change return status to used and give 20% discount for being used. 
product3.return_product().display_info()