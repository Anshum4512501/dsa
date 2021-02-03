def createstack():
    stack = []
    return stack

def isempty(stack):
    return True if len(stack) else False

def push(stack,element):
    stack.append(element)

def pop(stack):
    if isempty(stack):
        print("Stack is already empty")
        return None
    
         

stack = createstack()
print(isempty(stack))

