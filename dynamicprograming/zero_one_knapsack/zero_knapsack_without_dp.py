def find_max_profit(capacity,weight_of_item,value_array,number_of_items):
    
    if number_of_items == 0 or capacity == 0:
        return 0

    
    if weight_of_item[number_of_items-1] > capacity:
        return find_max_profit(capacity,weight_of_item,value_array,number_of_items-1)
    return max(value_array[number_of_items-1]+find_max_profit(capacity-weight_of_item[number_of_items-1],weight_of_item,value_array,number_of_items-1),find_max_profit(capacity,weight_of_item,value_array,number_of_items-1))        
   



capacity = 6
weight_of_item = [1,2,4,3,8]
value_array = [3,2,5,4,18]
number_of_items = len(value_array)
max_prof = find_max_profit(capacity,weight_of_item,value_array,number_of_items)
print(max_prof)
print(range(number_of_items))


# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


# def knapSack(W, wt, val, n):

# 	# Base Case
# 	if n == 0 or W == 0:
# 		return 0

# 	# If weight of the nth item is
# 	# more than Knapsack of capacity W,
# 	# then this item cannot be included
# 	# in the optimal solution
# 	if (wt[n-1] > W):
# 		return knapSack(W, wt, val, n-1)

# 	# return the maximum of two cases:
# 	# (1) nth item included
# 	# (2) not included
# 	else:
# 		return max(
# 			val[n-1] + knapSack(
# 				W-wt[n-1], wt, val, n-1),
# 			knapSack(W, wt, val, n-1))

# # end of function knapSack


# #Driver Code
# val = [3,2,5,4]
# wt = [1,2,4,3]
# W = 6
# n = len(val)
# print(knapSack(W, wt, val, n))

# # This code is contributed by Nikhil Kumar Singh
