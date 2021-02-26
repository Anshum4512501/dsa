def createstack():
    return []

def push(stack,element):
    stack.append(element)

def pop(stack):
    if not isempty(stack):
        stack.pop()
        

def isempty(stack):
    return True if len(stack) else False

def sorting(s):
    pass

s = createstack()
s.append(1)
s.append(2)
s.append(3)

print(s)
