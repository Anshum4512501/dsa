
# testcases = int(input())

testcases = 3
number = [3,3,5]
integers = ['2 7 5','3 3 3','2 2 2 2 5']
def find_triplet(arr, n): 
    s = set()
    for i in range(0, n): 
      
        for j in range(0, n): 
            for k in range(0, n): 
          
                if (i != j and k>j): 
                    s.add((arr[i],arr[j],arr[k]))
                
    return s

    
for _ in range(testcases):
    # number = int(input())
    for num in number:
        for x in integers:
            list_of_integers = list(map(int,x.split()))
            s = find_triplet(list_of_integers,len(list_of_integers))
            print(s)
            item_sum = []
            for item in s:
                
                i_sum = abs(item[0]-item[1])+abs(item[1]-item[2])+abs(item[2]-item[0])
                item_sum.append(i_sum)
        
    print(max(item_sum))    
         