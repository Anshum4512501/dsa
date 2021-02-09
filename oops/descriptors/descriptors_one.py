class IntegerField:
    def __set_name__(self,owner,name):
        self.name = name

    def __get__(self,instance,owner):
        print("__get__ called")
        return instance.__dict__.get(self.name,None)

    def __set__(self,instance,value):
        print("set called")

        if not isinstance(value,int):
            raise TypeError("value must be an integer")
        instance.__dict__[self.name] = value

class Point:
    x  = IntegerField()
    y  = IntegerField()

    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(10,20)         
print(p.x)
print(p.y)


        