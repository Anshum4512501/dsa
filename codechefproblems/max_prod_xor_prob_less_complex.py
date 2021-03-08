testcases = int(input())

def find_max(number):
    a = 2
    while True:
        if a < number:
            a = a << 1
        else:
            break
    mid = (a-1)>>1
    A = mid ^ number
    print(A*mid)
        
    
for _ in range(testcases):
    number = int(input())
    find_max(number)

    