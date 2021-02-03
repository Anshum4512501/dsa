class Employee(object):

    def __init__(self,name,age,occupation):
        self._name = name
        self._age  = age
        self._occupation = occupation

    def __str__(self):
        return self._age
        
    def show_details(self):

        return self._name+" " + self._age + self._occupation
        



emp = Employee("Anshoo Mishra",23,"SE")

print(emp.show_details())

