def squre(seq,index):
    return seq[index]**2

def squres(seq,max_length):
    for i in range(max_length):
        try:

            yield squre(seq,i)
        except Exception as ie:
            print(ie.__class__,"Error")    


l = [1,2,'1',3]

print(list(squres(l,4)))