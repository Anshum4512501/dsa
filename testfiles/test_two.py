class Test:
    t = 1 

    def __init__(self,t):
        self.t = t
    def show_content(self):
        return self.t

t = Test("Anshoo") 
print(t.show_content())

print(Test.t)