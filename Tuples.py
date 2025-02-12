#tuplles are ordered ,immutable and allow duplicates
mycourses=("html","css","javascript","python","django")
print(mycourses)
print(type(mycourses))
#accessing items
print(mycourses[1])
print(mycourses[2:])
#loop
for i in mycourses:
    print(i)
    #tuple contructor
    mynumbers=tuple((45,7,9,34,9,55))
    print(mynumbers)
    print(type(mynumbers))
    #loop throuygh the items
    for x in mynumbers:
        print(x)



