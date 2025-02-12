#lists are ordered,mutable and allow duplicates
students=["grace", "john","mark", "mark"]
print(students)
#accessing the items
print(students[0])
print(students[2])
print(students[-1])
#lens()
print(len(students))
#adding items
#append() add to the end
students.append("doreen")
print(students)
#insert(add item at a given index
students.insert(0,"nigel")
students.insert(3,"grace")
print(students)
#change a item
students[2]="alex"
print(students)
#remove list item
students.remove("mark")
print(students)
#pop()remove the last item
students.pop()
print(students)
#sort()
students.sort()
print(students)
#copy
mynewstudents=students.copy()
print(mynewstudents)
#list constructor
fruits=list(("oranges","apples" ,"pears" ,"bananas"))
print(fruits)
print(type(fruits))
#join lists extend() adds a second list at the end of the first list
mynewstudents.extend(fruits)
print(mynewstudents)
#clear
mynewstudents.clear()
print(mynewstudents)
#loop through the list items
for x in students:
    print(x)