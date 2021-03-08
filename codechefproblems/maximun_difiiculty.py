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