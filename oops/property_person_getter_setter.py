# from inspect import getclosurevars
# class Person:
#     def __init__(self,name):
#         self.name = name 


#     def getname(self):
#         print("Getter...")
#         return self._name 

#     def setname(self,value):
#         print("Setter...")
#         self._name = value


#     def delname(self):
#         del self._name


#     name = property(fget=getname,fset=setname,fdel=delname)
# print(getclosurevars(Person))
# p = Person("Anshoo")
# print(p.__dict__)
name = "Guido"

class Person:
    name = "Alex"
    list_one = [name]*3
    list_two = [name for i in range(3)] # name is from outer of this class

    @classmethod
    def hello(cls):
        print("{} says hello ".format(name))
        print(cls.list_one)
        print(cls.list_two)


Person.hello()


