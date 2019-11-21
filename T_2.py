import time

start_time = time.time()
a = 1
b = 2
sm = 2
while b<4000000:
    a,b = b,a+b
    if b%2== 0:
        sm+=b
print("answer: ",sm)
print(time.time() - start_time)
