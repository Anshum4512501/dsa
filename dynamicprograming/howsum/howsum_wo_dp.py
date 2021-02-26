import logging
logger = logging.Logger("how sum without dp")

def howsum(target_sum,arr):
    if target_sum == 0 : return []
    if target_sum < 0 :return None

    for item in arr:
        remainder = target_sum - item
        result = howsum(remainder,arr)
        
        if result != None:
            result.append(item)
            return result
            
            


    return 


hsum  = howsum(7,[4,3,2])
print(hsum)    

