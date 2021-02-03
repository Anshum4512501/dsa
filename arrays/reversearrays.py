# def reverse(arr):
#     start = 0
#     end   = len(arr)-1
#     while end-start >= 0 :
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp
        
#         start = start +1
#         end = end - 1
    
#     return arr

# arr = reverse([1,2,3,4,5,6,4,34,32,12,34,33,333,444,5,0,1,2,0,34])
# print(arr)
# problem code FLOW017
testcases = int(input())
for testcase in range(testcases):
    number = list(input())
    
    start  = 0
    end    = len(number) - 1
    while end-start >= 0 :
        temp = number[start]
        number[start] = number[end]
        number[end] = temp
        
        start = start +1
        end = end - 1
        newnumber = "".join(number)
    print(int(newnumber))  