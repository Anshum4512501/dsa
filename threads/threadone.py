import time
import threading

start = time.perf_counter()
def dosomethimg(sec):
    print(f"sleeping for{sec} seconds")
    time.sleep(sec)
    print("Done Sleeping .....")

threads = []

for _ in range(10):
    t = threading.Thread(target=dosomethimg,args=[1.4])
    t.start()
    threads.append(t)

for t in threads:
    t.join()    


end = time.perf_counter() - start

print(f"Done after {round(end,2)}")

























# t1 = threading.Thread(target=dosomethimg)
# t2 = threading.Thread(target=dosomethimg)

# t1.start()
# t2.start()
# t1.join()
# t2.join()