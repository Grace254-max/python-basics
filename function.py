#functionde

def myfunction():
    print("hello this a function")
#calling the function
myfunction()
myfunction()
#another function
#creating a function
def hello():
    print("hello goodmorning")
#calling the function
hello()
#another function
#creating a function
def sparkly():
    print("stars are beautiful")
#calling the function
sparkly()
#function with parameter
def greeting(fname):
    print("hello goodmorning",fname)
greeting("jane")
greeting("luke")
greeting("mary")
#funtion with two parameters
#a function that calculates area of a rectangle
def areaofrectangle(l,w):
    print("the area of rectangle with length",l,"and width",w,"is",l*w)
#calling the function
areaofrectangle(50,20)
areaofrectangle(100,50)
#function with a default parameter
def functionexample(name="mary",age=20):
    print("hello",name,"you age is",age)
#calling the function
functionexample("jane",20)
functionexample()
functionexample("andrew",19)
#return
def example(x):
    return x*5
#result=example(5)
#print(result)
print(example(2))
print(example(10))