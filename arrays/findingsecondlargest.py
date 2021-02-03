# Three numbers A, B and C are the inputs. Write a program to find second largest among them.
# code chef problem

testcases = int(input())
def secondlargestnumber(arr):
    max_index = arr.index(max(arr))
    arr.pop(max_index)
    return max(arr)
    
for testcase in range(testcases):
    arr = []
    for _ in range(3):
        arr.append(int(input()))
    
    secondlargest = secondlargestnumber(arr)
    print(secondlargest)