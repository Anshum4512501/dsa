# class ContextManager(object):
#     def __init__(self,listname):
#         self.listname = listname
#     def __enter__(self):
#         return self.listname
#     def __exit__(self,a,b,c):
#         print("Cleanup code here")

# with ContextManager([1,2,3]) as a:
#     print(a)


from contextlib import contextmanager

@contextmanager
def open_file(filename,mode):
    f = open(filename,mode)
    yield f
    f.close()

with open_file('test.txt','w') as f:
    f.write("Testing")

