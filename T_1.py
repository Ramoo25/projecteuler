import time


#First solution
start_time = time.time()
print(sum(n for n in range(1,1000) if (n%3==0 or n%5==0)))
print(time.time()-start_time)


print("")
print("")
print("")


#Second solution
start_time = time.time()
i=1
sm = 0
while (i < 1000):
    if (i%3 == 0) or (i%5 == 0):
        sm += i
    i += 1
print("answer: ",sm)
print(time.time()-start_time)


print("")
print("")
print("")


#Third solution
start_time = time.time()
sm = 0
chi = (3,5)
muli = []
for i in range(len(chi)):
    for j in range(i+1,len(chi)):
        muli.append(chi[i]*chi[j])
for z in chi:
    mx = 999
    while True:
        if mx%z == 0:
            sm += int(((z+mx)//2)*(mx//z))
            break
        mx -= 1
for z in muli:
    mx = 999
    while True:
        if mx%z == 0:
            sm -= int(((z+mx)/2)*(mx/z))
            break
        mx -= 1
print("answer", sm)
print(time.time()-start_time)
