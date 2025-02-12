class Employee:
    def __init__(self,name,age,salary,job_title):
        self.name = name
        self.age =age
        self.salary = salary
        self.job_title= job_title
    def dispayinfo(self):
        print(f"name{self.name}")
        print(f"age:{self.age}")
        print(f"salary:{self. salary}")
        print(f"job_title:{self.job_title}")
    def increase_salary(self,amount):
        self.salary += amount
        print(f"the salary of {self.name} has increrased to {self.salary}")
    def get_annual_salary(self):
        return self.salary *12
    def change_name(self,new_name):
        self.name = new_name
        print(f"Employee name updated to {self.name}")
    def change_title(self,new_job_title):
        self.job_title = new_job_title
        print(f"{self.name} new job title is {self.job_title} ")


#create an object
emp1=Employee( "catherine",21,40000,"accounting")
emp2=Employee("john",21,100000,"IT")
#accessing the attributes
print(emp1.name)
print(emp2.name)
#calling dispayinfo() object.method name
emp1.dispayinfo()
emp2.dispayinfo()
#increase salary by given amount
emp1.increase_salary(10000)
emp2.increase_salary(50000)
#get and print annual salary
print(f"the annual salary of {emp1.name} is {emp1.get_annual_salary()}")
print(f"the annual salary of {emp2.name} is {emp2.get_annual_salary()}")
emp1.dispayinfo()
emp2.dispayinfo()
#change employee name
emp1.change_name("mary")
#diplay updated info
emp1.dispayinfo()
emp2.dispayinfo()
#change title
emp2.change_title("programmer")
#display updated info
emp2.dispayinfo()
#inherit from employee class
class Manager(Employee):
    def __init__(self,name ,age,salary,job_title ,team_size):
        super().__init__(name,age,salary, job_title)
        self.team_size=team_size
    def dispayinfo(self):
        super().dispayinfo()
        print(f"team size: {self.team_size}")
#create an object
mgr=Manager("jack",20,70000,"manager",10)
mgr.displayinfo()

