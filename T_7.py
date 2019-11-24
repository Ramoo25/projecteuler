import time
#104743
start_time = time.time()

mas = []

num_max = 10001  #STOP CONDITION
n_mas = 30000      #count in one cicle
start_mas = 2  #const

u = []

for i in range(0,n_mas):
  mas.append(start_mas+i)
for i in range(len(mas)):
  if mas[i]==0:
    continue
  u.append([mas[i],0])
  j = i
  for j in range(i+mas[i],len(mas),mas[i]):
    mas[j] = 0
  u[len(u)-1][1]=j+2

#print("mas",mas)
start_mas += n_mas
kol = 0
flag = False
for i in range(len(mas)):
  if mas[i] != 0:
    kol += 1
  if kol == num_max:
    print("answer: ", mas[i])
    flag = True
    break
n = 1
while not flag:
  for i in range(0,n_mas):
    mas[i] = start_mas+i
  for i in range(len(u)):
    step = u[i][0]
    poz = u[i][1]
    poz += step
    #print(step,poz)
    #print(poz-n*n_mas-2)
    while poz < start_mas+n_mas:
      mas[poz-n*n_mas-2] = 0
      poz += step
    u[i][1] = poz-step
  flag = False
  for i in range(len(mas)):
    if (mas[i]!=0):
      kol += 1
      u.append([mas[i],mas[i]])
      if kol == num_max:
        print("answer: ",mas[i])
        flag = True
        break        
  n+=1
  start_mas += n_mas
  #print ("mas",mas)

#print (mas)
print(time.time()-start_time)
