testcases = int(input())

def find_max(number):
    a = 2
    max_product = -1
    while True:
        if a < number:
            a = a << 1
        else:
            break
    for item in range(1,a//2):
        A = item ^ number
        
        product = A*item
        print("product is",product)
        if product > max_product:
            max_product = product

    return max_product        
        
    
for _ in range(testcases):
    number = int(input())
    max_product = find_max(number)

    print(max_product)