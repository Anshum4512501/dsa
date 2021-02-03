# Without using dynamic programming

class GridTraveller:
    
    def gridtraveller(self,m,n):
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1 :
            return 1

        return self.gridtraveller(m-1,n) + self.gridtraveller(m,n-1)

gt = GridTraveller()
ways =  gt.gridtraveller(18,18)                    

print(ways)


# Using dynamic programming

class GridTravellerUsingDP:
    def gridtraveller(self,m,n,memo = {}):
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1 :
            return 1
        # creaing key like m,n 
        key = str(m)+ ',' + str(n)   
        if key in memo:
            return memo[key]

        memo[key] = self.gridtraveller(m-1,n,memo) + self.gridtraveller(m,n-1,memo)
        return memo[key]     


# gt = GridTravellerUsingDP()
# ways =  gt.gridtraveller(18,18)        

# print(ways)