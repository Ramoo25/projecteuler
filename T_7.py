import time

start_time = time.time()
x = 2
i = 3

while (x <= 10001):
  z = 2
  while (z < int(i**0.5)+1):
    if (i % z == 0):
      break
    z += 1
  else:
    x += 1
  i += 1


print("answer: ",i-1)
print(time.time()-start_time)
