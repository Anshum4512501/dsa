testcases = int(input())

def find_groups(string):
    groups = [0]
    index = -1
    for item in string:
        index += 1
        if item == '0':
            
            continue
        if item == '1':
            
            test_next_zero_or_one(string,groups,index)
    
    print(groups[0])
def test_next_zero_or_one(string,groups,index):
    if index == len(string)-1:
        groups[0] = groups[0]+1
    else:
        
        index = index + 1
        if string[index] == '0':
            groups[0] = groups[0]+1
        
    
for _ in range(testcases):
    
    string = input()
    
    find_groups(string)
    
    
    
        
        
        