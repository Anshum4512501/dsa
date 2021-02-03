# Adding two numbers recursivily

def add(x,y):
    if x == 0:
        return y
    return add(x-1,y+1)

print(add(2,10))
