def outer(*args,**kwargs):
    print("I am outer function")
    def innerfunction(function):
        print("I am innerfunction taking arguments from outer function",kwargs["me"])
        function()
    return innerfunction

@outer(me="Anshoo Mishra")
def callme(*args,**kwargs):
    print(args)




