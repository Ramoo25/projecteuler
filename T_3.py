import time

def is_prime(x):
  for j in range(2,int(x**0.5)+1):
    if (x%j == 0):
      return False
  return True

start_time = time.time()

num = 600851475143
mx = 0
while True:
    dl = 2
    while (dl < num//2):
        if num%dl==0:
            num = num//dl
            if dl>mx and is_prime(dl):
                mx = dl
            break
        dl += 1
    else:
        if num > mx:
            mx = num
            break
print("answer: ",mx)
print(time.time() - start_time)
