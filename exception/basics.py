def test_exception(a,b):

    print("I am inside test exception function")
    divide(a,b)

def divide(a,b):
    result = a/b
    return result


test_exception(1,0)
