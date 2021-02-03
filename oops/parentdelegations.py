class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("Every A eats does not matter weather it is {}".format(self.__class__.__name__))
    
    def walk(self):
        print("Every A walks does not matter weather it is {}".format(self.__class__.__name__))
        

class B(A):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno = rollno

    def occupation(self):
        print(self.name + " is {}".format(self.__class__.__name__))  
    
    def walk(self):
        print("Every B walks does not matter weather it is {}".format(self.__class__.__name__))
    

# class C(B):
    
#     super(B,a).walk()



# c = C("Anshoo Mishra",30,12501)
# c.eat()
# c.occupation()          
