def max_heapify(arr,i):
    left = 2*i + 1
    right = 2*i + 2 

    if left <= len(arr)-1 and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right <= len(arr)-1 and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        max_heapify(arr,largest)
def delete_from_max_heap(arr,key):
    index_in_heap =  arr.index(key)
    arr[index_in_heap] = arr[len(arr)-1]
    arr.pop(len(arr)-1)
    max_heapify(arr,index_in_heap)

arr = [1,2,3,4,5,6]
for i in range((len(arr)-2)//2,-1,-1):

    max_heapify(arr,i)
print(arr)

delete_from_max_heap(arr,6)
print(arr)
            