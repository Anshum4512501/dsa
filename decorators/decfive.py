def outerdecoratorfunctionwitharguments(a,b):

    def wrapper(function):

        def innerfunction(*args):
            return function(*args)
        return innerfunction
    return wrapper    


@outerdecoratorfunctionwitharguments(1,2)
def testme(a,b):
    print("I am test me function having ",a,b)


testme = outerdecoratorfunctionwitharguments(1,2)(testme)
testme(5,6)
# testme(1,2)
