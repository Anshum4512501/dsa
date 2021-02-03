import concurrent.futures
import time

start = time.perf_counter()
def dosomething(sec):
    print(f"sleeping for {sec} seconds")
    time.sleep(sec)
    print("Done sleeping....")


with concurrent.futures.ThreadPoolExecutor() as executer:
    f1 = executer.submit(dosomething,1)
    print(f1.result())


end = time.perf_counter()
print(f"finished in {round(end-start,2)}")

