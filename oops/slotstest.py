# class Point:
#     __slots__ = ('x','y','__dict__')
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


# p = Point(1,2)
# p.z = 100
# print(p.x)
# print(p.y)
# print(p.__dict__)

class Person:
    __slots__ = "_name","age",

    def __init__(self,name ,age):
        self.name = name 
        self.age = age

    @property
    def name(self):
        return self._name.upper()

    @name.setter
    def name(self,name):
        self._name = name

p = Person("Anshoo",34)
print(p.name)            

