import time

start_time = time.time()

stop = 500
n = 1
while True:
  tch = int((n+1)*n*0.5)
  kol = 2
  for j in range(2, int(tch**0.5)+1):
    if (tch % j == 0):
      kol += 2
  if (kol > stop):
    break
  n += 1

print ("answer: ",tch)
print(time.time()-start_time)
