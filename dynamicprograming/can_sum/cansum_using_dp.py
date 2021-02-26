def cansum(target_sum,arr,memo={}):
    if target_sum == 0:
        return True

    for item in arr:
        if item > target_sum:
            continue
        elif cansum(target_sum-item,arr) == True:
            return True

    return False        
           
arr = [7,5,77]

val = cansum(30,arr)

print(val)
