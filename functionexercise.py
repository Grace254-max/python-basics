#a function that adds two numbers
#function that calculate area of square
#function that determines if a no is even or odd(num1&2)
#a function that determines maximum of two numbers
#a function that calculates area of a circle(3.142*r*r)

def maxnumber(num1,num2):
    return max(num1,num2)
print(maxnumber(500,200))

def sumofnumbers(num3,num4):
    print("the sum of",num3, "and", num4,"is",num3+num4)
#calling the function
sumofnumbers(50,50)

def areaofsquare(s):
    print(" the area of square with side",s,"is",s*s)
#calling the function
areaofsquare(50)

def areaofcircle(r):
    print("the area of a circle with",r,"is",3.142*r*r)
#calling the function
areaofcircle(14)
areaofcircle(500)



def evenorodd(x):
    if x%2==0:
        print(x,"is odd")
    else:
        print(x,"is odd")
evenorodd(10)
evenorodd(7)


def addtwomumbers(a,b):
    return a+b
print(addtwomumbers(10,30))
#lambda function/anonymous function
#lambda funtion adds two numbers
x=lambda a,b:a+b
print(x(50,40))
#lambda function that adds three numbers
y=lambda a,b,c:a+b+c
print(y(50,60,80))
#lambda function than multiplies two no
w=lambda e,f:e*f
print(w(60,4))




