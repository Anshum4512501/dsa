# calculating fib without using dynamic programming

def findfibwithoutdp(n):
    if n <= 2:
        return 1

    return findfibwithoutdp(n-1) + findfibwithoutdp(n-2)    

# Calculating fib using dynamic programming
import sys

def find_fib(n,memo = {}):
    if n in memo:
        return memo[n]

    if n<=2 :
        return 1

    memo[n] =  find_fib(n-2,memo) + find_fib(n-1,memo)
    
    return memo[n]
# print(find_fib(50))     
print(findfibwithoutdp(50))     
# print(sys.stdout.write("AAAA\n"))
# sys.stdout.flush()