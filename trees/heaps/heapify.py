def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2


def max_heapify(arr,i):
    l = left(i)
    r = right(i)
    if l <= len(arr)-1 and arr[i] < arr[l]:
        largest = l
    else:
        largest = i
    if r <= len(arr)-1 and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        max_heapify(arr,largest)
        
arr = [16,4,10,14,7,9,3,2,8,1]
for i in range((len(arr)-2)//2,-1,-1):

    max_heapify(arr,i)


print(arr)    