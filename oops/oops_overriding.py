class Person:
    def __repr__(self):
        return f"{self.__class__.__name__} class"

class Student(Person):
    pass

s = Student()
print(s.__str__())

