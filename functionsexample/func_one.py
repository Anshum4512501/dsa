lam = lambda x : x*2

# print(lam(2))

def _addition(x,y):
    assert isinstance(x , int) and isinstance(y,int) 
    return x + y

def get_add(x,y):
    _addition(x,y)

map(get_add,[1,2,3,4])

# get_add(1,2)

def test(me,you,they=[]):
    if they:
        print("there is a third party is waiting {}".format(they))
    else:
        print("Me {} and you {} only are here".format(me,you))


test("Anshoo","Anjali",they=["balesh","vijay"])           
