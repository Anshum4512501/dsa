def insertion_sort(arr):
    for j in range(1,len(arr)-1):
        key = arr[j]
        i = j-1

        while i > 0 and arr[i] >key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key
    
arr  = [12,2,13,3,14]        
insertion_sort(arr)
print(arr)