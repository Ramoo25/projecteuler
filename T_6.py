import time

start_time = time.time()
print("answer: ",int(sum(i for i in range(1,101)))**2-sum(i**2 for i in range(1,101)))
print(time.time()-start_time)

