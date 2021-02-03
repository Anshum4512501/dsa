from math import pi

class Circle(object):
    def __init__(self,radius):
        self._radius = radius
        self._area   = None

    @property
    def radius(self):
        if not isinstance(self._radius,str):

            return abs(self._radius)
        raise ValueError("radius can not be string")


    @radius.setter
    def radius(self,radius):
        self._area = None
        self._radius = radius

    @property
    def area(self):
        if self._area is None:
            print("Calculating area")
            self._area = pi*self.radius**2
        
        return self._area


# c =Circle(2)
# print(c.area)
# print(c.area)
# c.radius = 12
# print("\n")
# print(c.area)




