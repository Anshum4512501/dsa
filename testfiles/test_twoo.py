# a = []
# a.extend([1,2,3])
# a.append([2,3])
# a.extend([5,6,7])
# print(a)
class ListSubstration:
    def __init__(self,list_one) -> None:
        self.list_one = list_one


    def __sub__(self,other):
        if len(self.list_one)!= len(other):
            raise NotImplementedError
        return [x1-x2 for x1,x2 in zip(self.list_one,other) ]    


list_one = ListSubstration([1,2,3])
try:
    print(list_one-[2,3])

except NotImplementedError:
    print("Error")    
    



