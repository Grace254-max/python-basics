
#if executes a block of code if the given condition is true
#if condition:
        #block of code to be executed
        #if the condition is true
x=3
if x<5:
    print(x,"is less then 5")
    #else :specifies the block of code to be executed
    #if the condition is false
    i=8
    if i>10:
        print(i,"is greater than 10")
    else:
        print(i, "is less than 10")
        #a program that asks user age,if age is greater than or equal to
        #equal to 18,user can drive else they cannot
age=int(input("what is your age?"))
if age>=18:
    print("you can drive")
else:
    print("you can not drive")
    #write a program that get a number from user that checks if
    #its odd or even number
num1=int(input("enter first number"))
if num1%2==0:
    print(num1,"is even")
else:
    print(num1,"is odd")
    #write a program that gets two numbers from user then checks which one is greater
    num2=int(input("enter second number"))
    num3=int(input("enter second number"))
    if num2>num3:
        print(num2 ,"is greater")
        print(num3,"is lesser")



