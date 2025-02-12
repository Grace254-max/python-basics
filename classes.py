#class is a blueprint for creating sth
#object is an instance of a class
#student class:first name,second name,course ,age
from dictionary import student


class Student:
    def __init__(self,first_name,last_name,age,course):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.course=course
    def __str__(self):
        return F"{self.first_name}{self.last_name}{self.age}{self.course}"
    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"
    def intro(self):
        print(f"hello my name is {self.first_name} and i`m learning {self.course}")
    def get_email(self):
        return f"{self.first_name} {self.last_name} @emobilids.ac.ke"



#create an object
student1=Student("ruth", "kamau", 30, "fullstack")
student2=Student("dan", "john", 18, "data analyst")
print(student1)
print(student2)
#accessing attributes value
print(student1.first_name)
print(student2.last_name)
#calling a method
print(student1.get_full_name())
print(student2.get_full_name())
student1.intro()
print(student1.get_email())
print(student2.get_email())

