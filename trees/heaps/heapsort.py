# O(log(n)) times run min_heapify
def min_heapify(arr,i):
    left  = 2*i + 1 
    right = 2*i + 2 

    if left < len(arr)-1 and arr[left] < arr[i]:
        smallest = left
    else :
        smallest = i

    if right < len(arr) - 1 and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        temp = arr[smallest]
        arr[smallest] = arr[i] 
        arr[i] = temp
        min_heapify(arr,smallest)


# O(n) times not the order of nlog(n)
def buildheap(arr):
    for i in range((len(arr)-1//2),-1,-1):
        min_heapify(arr,i)

# (TO DO) Heap Sort Code

