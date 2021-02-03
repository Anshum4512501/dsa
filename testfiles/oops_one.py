from typing import Any
class Employee(object):
    def __init__(self,f_name:str,l_name:str,age:int)->Any:
        self.f_name:str = f_name 
        self.l_name:str = l_name 
        self.age:int    = age

    @property
    def show_details(self)->Any:
        print(self.f_name+" "+self.l_name)


emp = Employee("Anshoo","Mishra","")

emp.show_details