# Rearranging array as a[i] = i

# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
#               11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#          11, 12, 13, 14, 15, 16, 17, 18, 19]

# O(n) time complexity
# O(n) space complexity


def rearrange(arr):
    brr = [None]*len(arr)
    for item in arr:
        if item != -1:
            brr[item] = item

    for i in range(len(brr)):
        if brr[i] == None:
            brr[i] = -1



    print(brr)

rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])                
rearrange([19, 7, 0, 3, 18, 15, 12, 6, 1, 8,\
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4])