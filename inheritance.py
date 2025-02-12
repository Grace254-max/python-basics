#parent/super class
class animal:
    def __init__(self,name):
        self.name = name
    def supermethod(self):
        print("hello from super class")
    def speak(self):
        print("hello hello")
#a child class that inherits from animal class
class Dog(animal):
    def submethod(self):
        print("hello from sub class")
    def speak(self):
        print(f"{self.name} does gugu! gugu!")

#create an object
mydog=Dog ("Bob")
print(mydog.name) #inherited name attribute
#calling a method in the parent class
mydog.supermethod()
mydog.speak()
class cat(animal):
    def speak(self):
        print(f"{self.name} says meow meow" )
mycat=cat("parsley")
print(mycat.name)
#calling am method in the parent class
mycat.supermethod()
mycat.speak()
