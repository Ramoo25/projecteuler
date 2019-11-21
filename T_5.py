import time
#2*3*5*7*11*13*17*19 = 9699690

start_time = time.time()

x = 0
d = (20,18,16,12)
'''
4 in 20,16,12
6 in 18,12
8 in 16
9 in 18
10 in 20
'''

flag = True

while True:
  x += 9699690
  for i in range (0,len(d)):
    if (x % d[i] != 0):
      break
  else:
    break

print("answer: ",x)
print(time.time() - start_time)
