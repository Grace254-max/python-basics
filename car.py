class Car:
    def __init__(self,color,brand):
            self.color=color
            self.brand=brand
    def carinfo(self):
             return f"this is a {self.color} {self.brand}"
#create objects
car1=Car("yellow","BMW")
car2=Car("red","toyota")
#accessing the attributes
print(car1.color)
print(car1.brand)
print(car2.color)
print(car2.brand)
#calling the carinfo method
print(car1.carinfo())
print(car2.carinfo())


