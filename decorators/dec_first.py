def outerfuntion(originalfunction):
    print("I am outer function")

    def innerfunction(*args):
        print("I am inner function")
        return originalfunction(*args)
    
    return innerfunction
@outerfuntion
def displaycontent(a,b):
    print("I am displaycontent function")

# displaycontent = outerfuntion(displaycontent)    

displaycontent(1,2)