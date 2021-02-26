def canconstruct(target_string:str,arr_of_string):
    if target_string is None:
        False
    if len(target_string) == 0:
        return True

    for item in arr_of_string:
        if target_string.find(item) == 0:
            string = target_string[len(item):]
            if canconstruct(string,arr_of_string) == True:
                return True

    return False


val1 = canconstruct('abcdef',['ab','abc','cd','def','abcd'])
val2 = canconstruct('abcdef',['ab','abc','cd','abcd'])
print(val1)
print(val2)