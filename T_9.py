import time

start_time = time.time()

b = 499
a = 0
c = 0
#First solution (some math)

while b > 0:
  if ((1000*b-500000)%(b-1000))==0:
    a=(1000*b-500000)/(b-1000)
    c=1000-a-b
    print ("answer: ",int(a*b*c))
    break
  b -= 1

'''
#Second solution (bruteforce), very slow

flag = False
for a in range(1,997):
  for b in range(a,1000-a):
    c = 1000-a-b
    if (a*a+b*b==c*c):
      print("answer: ",a*b*c)
      flag = True
      break
  if flag:
    break
'''

print(time.time()-start_time)
