class Duck:

    def quack(self):
        print("Quack Quack")
    def fly(self):
        print("Fly Fly")


class Person:
    def quack(self):
        print("Quack like duck")

    def fly(self):
        print("fly like a duck")

# def quack_and_fly(thing):
#     if isinstance(thing,Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print("There is no duck at all")

#     print()

# NON PYTHONIC WAY TO SOLVE THIS ISSUE

# def quack_and_fly(thing):
#     if hasattr(thing,'quack'):
#         if callable(thing.quack):
#             thing.quack()
#     if hasattr(thing,'fly'):
#         if callable(thing.fly):
#             thing.fly()  


#PYTHONIC WAY TO SOLVE THIS ISSUE

def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)
d = Duck()
quack_and_fly(d)      

p = Person()
quack_and_fly(p)