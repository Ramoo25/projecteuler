import time
start_time = time.time()


#First solution (fast)
a = []
mx = 2000001

i = 0
a = [i for i in range (2,mx)]
  
for i in range(0,len(a)):
  if a[i] != 0:
    j = i
    while True:
      j += a[i]
      if j<len(a):
        a[j]=0
      else:
        break
        
sum = 0        
for i in range(0,len(a)):
  sum += a[i]

print("answer: ",sum)

'''
#Second solution (very very slow)
sum = 2
i = 3

while i<2000000:
  j = 2
  while j<int(i**0.5)+1:
    if (i%j==0):
      break
    j += 1
  else:
    sum += i
  i += 2

print ("answer: ",sum)
'''

print (time.time()-start_time)
