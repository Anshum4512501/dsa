def fun(n,memo = {}):
    if n == 0:
        return 1
    q = 0

    for i in range(1,n+1):
        if n in memo:
            return memo[n]
        memo[n] = fun(n-i)    
        q = q + memo[n]    

    return q

# val =fun(4)

# print(val)



