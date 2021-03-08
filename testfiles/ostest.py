# testcases = int(input())

# def isnegative(number):
#     if number < 0:
#         return True
        
#     return False
    
# def find_least_number(number,attempt):
#     if number == 0 :
#         return 0
#     if number-attempt < attempt and not isnegative(number-attempt):
        
#         return number-attempt
#     elif attempt > number:
#         return number
        
#     return find_least_number(number-attempt,attempt)    
# def code_start():
    
    
#     for _ in range(testcases):
    
#         n, k = input().split(" ")
#         n = int(n)
#         k = int(k)
    
#         print(find_least_number(n,k))
    
    
# code_start()    
    
        
        
        
            


# testcases = int(input())

def find_maximum_difficulty(arr,k,length):
    
    if int(arr[length-1]) == 0:
        if length-1>0:
            return find_maximum_difficulty(arr,k,length-1)
    if k<=0:
        if int(arr[length-1])!=0:
            return length
        else:
            return find_maximum_difficulty(arr,k,length-1)    
    k = k - int(arr[length-1])
    return find_maximum_difficulty(arr,k,length-1)
        
    
for _ in range(1):
    # list_of_number = input().split(" ")
    list_of_number = '2 0 1 0 0 0 0 0 0 10'.split(" ")
    # k = int(input())
    k = 12
    length = len(list_of_number)
    
    print(find_maximum_difficulty(list_of_number,k,length))