class Person:
    name = 'Person'

    def __init__(self,name):
        self.name  = name

class Teacher(Person):
    pass



p1 = Person("Anshoo")
print(p1.__dict__)
print(p1.name)
