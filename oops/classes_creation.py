classname = 'Circle'
class_body = """
def __init__(self,radius):
    self.radius = radius

def area(self):
    return self.radius*self.radius    

    """

class_dict = {}

class_bases = ()

exec(class_body,globals(),class_dict)

Circle = type(classname,class_bases,class_dict)

# print(help(Circle))

c = Circle(10)
print(c.area())


