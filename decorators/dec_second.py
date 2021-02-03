def star(function):
    def innerfunction(*args,**kwargs):
        print("*"*30)
        function(*args,**kwargs)
        print("*"*30)
    return innerfunction    


def percent(function):
    def innerfunction(*args,**kwargs):
        print("%"*30)
        function(*args,**kwargs)
        print("%"*30)
    return innerfunction

# @star
# @percent
def printme(*args,**kwargs):
    print(*args,**kwargs)
star(percent(printme))("Hello")

# printme("Hello")