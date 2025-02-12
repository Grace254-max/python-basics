#create a class project
#attributes:price,name,description,qu
#create objects
#add methods like dispayinfo(),totalprice,apply_discounts
#create objects


class Product:
    def __init__(self,name,price,description,quantity):
        self.name=name
        self.price=price
        self.description=description
        self.quantity=quantity
    def dispayinfo(self):
        print (f"name{self.name}")
        print(f"price{self.price}")
        print(f"description{self.description}")
        print(f"quantity{self.quantity}")
    def totalprice(self):
        return self.price*12
    def calculate_final_price(self,percentage):
        discount =self.price*percentage/100
        final_price=self.price-discount
        return final_price



#create an object
product1=Product("mug",20, "coffee mug","dozen")

print(product1)
#acessing the attributes
print(product1.name)
#calling dispayinfo() object.method name
product1.dispayinfo()
#print total price
print(f"the total price of {product1.name} is {product1.totalprice()}")



