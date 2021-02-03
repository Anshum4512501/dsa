def fun(a):
    a = 99
    print("function called here")
b = 100
fun(b)
print(b)
 

def another_fun(a):
    a[0] = 'a'

b = [1,2,3]

another_fun(b)
print(b)