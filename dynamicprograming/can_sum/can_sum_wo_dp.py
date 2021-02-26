def cansum(target_sum,arr):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for item in arr:
        remainder = target_sum - item
        if cansum(remainder,arr) == True:
            return True

    return False
arr = [7,14]

val = cansum(300,arr)

print(val)