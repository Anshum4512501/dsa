class A:
    attr = 1

class B(A):
    pass

class C(A):
    attr = 2

class D(B,C):
    pass

x = D()

print(x.attr)
print()



