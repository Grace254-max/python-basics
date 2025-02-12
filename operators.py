first_name="joyce"
hobbies="hiking"
print("my name is" , first_name, "i love" , hobbies)
#f string
print(f"my name is {first_name} i love {hobbies}")
#operators
#arithmetic operators+ / * / %
#addition +
x=10
y=30
sum=x+y
print(f"the addition of {x} and {y} is {sum}")
#-
print(f"the difference of {x} and {y} is {x-y}")
#multiplication
prod=x*y
print(f"the product of {x} and {y} {x*y}")
#division
div=y/x
print("the division of" , y,"and" ,x ,"is" , div)
#modulas:the remainder of division
a=3
b=2
print(f"ther modulas{a} and {b} is {a%b}")
#assignmen operators =+= -+= they assign values to variables
d=10
print(d)
d+=5 #d=d+5
print(d)
d-=10 #d=d-10
print(d)
#comparison aporators:used to compare two values
#= =,<,>,>=,<=
#equal==
print(f"is {x}equal to{y}?{x==y}")
#greater than >
print(f"is{x} greater than{y}?,{x>y}")
#less than <
print(f"is {x} less than {y}? {x<y}")
#greater than or equal to>=
print(f"is {x} greater than or equal to {y}? , {x>=y}")
#less than or equal to <=
print(f"is {x} less than or equal to {y}? ,{x<=y}")
#logical operators: AND,OR, NOT
#AND: returns if both statements are true
e=5
print(f"{e>3 and e<10}")
print(f"{e<3 and e<10}")
#or:returns true if one statement is true
print(e<3 or e<10)
#not reverses the result
f=True
print(f)
print(not(f))
