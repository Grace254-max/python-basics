#Dics are used to store data in key value pairs
#items are ordered, changeable and dot allow duplicate
student={
    "name":"jane",
    "age":20,
    "city":"nairobi"}
#accessing value
print(student["name"])
print (student["city"])
#print all keys.keys()
print(student.values())
#print all values
print(student.values())
print(type(student))
#print a list of key.value pairs
print(student.items())
#change items
student["name"]="ruth"
print(student)
#add item
student["course"]="fullstack"
print(student)
#print all the key one by one loop
#print all the values one by one
#print all key:value pair one by one
for x,y in student.items():
    print(x,y)





