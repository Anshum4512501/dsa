import time 
start = time.perf_counter()
def calcualtepowers(base):
    print(base**300)

calcualtepowers(5)
calcualtepowers(10)

end = time.perf_counter() - start

print(f"finished in {round(end,2)}")
