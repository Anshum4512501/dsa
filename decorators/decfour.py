# class decorator:

#     def __init__(self,func):
#         self.func = func

#     def __call__(self,*args):

#         self.func(*args)    


# class Decorator:
#     @decorator
#     def method(self):
#         print("I am decorator method")        


# d = Decorator()
# d.method()        

class decorator(object):
    def __init__(self,func):
        self.func = func


    def __call__(self,*args):
        
        print("I am inside call function {}".format(args))
        self.func(*args)

class C:
    @decorator
    def method(self):
        print("I am method from C")


c = C()
c.method()




# def display(a,b):
#     print("a = {},b = {}".format(a,b))



# dec = decorator("func")
# dec(1,2)