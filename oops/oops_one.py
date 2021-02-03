class OopsOne:
    c:str
    d:str
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def showdata(self):
        print(self.a,self.b)
        print(OopsOne)

    @classmethod    
    def classmem(cls):
        cls.c = "C"
        cls.d = "D"



o = OopsOne(1,2)
o.showdata()
print(OopsOne.c)
print(OopsOne.d)