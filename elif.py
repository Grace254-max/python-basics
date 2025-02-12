#elif:for adding another condition to test if
x=5
if x>10:
    print(x,"is greater than 10")
elif x==5:
    print(x,"is equal to five")
else:
    print(x,"is equal to five")

#write a program that asks eser for age then displays the
#following
#18-25=young adult
#26-40-adult
#41 and above mature
#below 18-a baby
age=int(input("what is your age?"))
if age>=18 and age<=25:
    print("hi!,you are a young adult")
elif age>=26 and age<=40:
    print("you are an adult")
elif age>40:
    print("you are mature")
else:
    print("you are a baby")
    #write a program that asks users for marks
    # then displays students grade according to marks
    #80-100=A
    #70-80=B
    #60-69=C
    #50-59=D
    #below 50=fail
marks=int(input("enter your marks"))
if marks>=80 and marks<=100:
    print("A")
elif marks>=70 and marks<=79:
    print("B")
elif marks>=60 and marks<=69:
    print("C")
elif marks>=50 and marks<=59:
    print("D")
else:
    print("fail")