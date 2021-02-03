class Person:
    language = 'python'
# self is always optional 
# but recommended to use this 

    def sayhello(obj,name):
        obj.name = name

    def saybye(self):
        pass



Person.otherfunc = lambda *args:print("I am labda function with {}".format(args))

p = Person()  
p.sayhello("Anshoo")
print(p.otherfunc())
print(p.__dict__)      

