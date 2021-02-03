# we are given an array of numbers and we need to find out weather 
# there is possibility to get target sum 
# example -- cansum(8,[3,4,5]) --> true
# cansum(9,[2,3,10]) --> false

def cansum(targetsum,numberlist):
    if targetsum == 0:
        return True
        