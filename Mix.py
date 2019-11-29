#вычисление факториала
def factorial (x):
  p = 1
  for i in range (1,x+1):
    p *= i
  return p







#сокращение дроби 8/16 -> 1/2
def sokrashenie(x,y):
  if (x>y):
    mini = y
    maxi = x
  else:
    mini = x
    maxi = y
    
  while True:
    flag = False
    for i in range (2,int(mini**0.5)+2):
      if mini%i==0:
        if maxi%i==0:
          mini = int(mini//i)
          maxi = int(maxi//i)
          flag = True
          break
    if flag == False:
      break
    
  if (x>y):
    return ([maxi,mini])
  else:
    return ([mini,maxi])









#поиск всех возможных составлений 200
#из кусочков m()
aim = 200
m = (1,2,5,10,20,50,100,200)
def finder(n,i):
  if n==0:
    return 1
  if n<0:
    return 0
  a = 0
  for j in range(0,i+1):
    a += finder(n-m[j],j)
  return(a)
#print (finder(aim,len(m)-1))






#число простое?
def is_prime(x):
  for j in range(2,int(x**0.5)+1):
    if (x%j == 0):
      return False
  return True








#следующее простое число
def next_prime(x):  
  i = x + 1
  while True:
    flag = False
    for j in range(2,int(i**0.5)+1):
      if (i%j == 0):
        flag = True
        break
    if flag == False:
      return (i)
    i += 1










#упрощает степени
#27^4->3^12
#144^3->12^6
def simple_pimple(i,j):
  for k in range(2,int(i**0.5)+1):
    d = i
    st = 1
    while True:
      if (d%k == 0):
        if d/k!=1:
          #print (d)
          d = d/k
          st += 1
        else:
          return [k,st*j]
      else:
        break
  return [i,j]







#возвращает список простых чисел в
#диапазоне (y,x)
def prime_num(y,x):  
  lst =[] 
  for i in range(y,x+1):
    flag = False
    for j in range(2,int(i**0.5)+1):
      if (i%j == 0):
        flag = True
        break
    if flag == False:
      lst.append(i)
  return lst










#число палиндром в бинарном виде
#например 585
def is_bin_palindrome(x):
  s = bin(x)
  s1 = s[::-1]
  if s[2:] == s1[:-2]:
    return (True)
  else:
    return (False)








#число палиндром?
def is_palindrome(x):
  s = str(x)
  if len(s)%2==0:
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    s2 = s2[::-1]
  else:
    s1 = s[:(len(s)-1)//2]
    s2 = s[(len(s)-1)//2+1:]
    s2 = s2[::-1]
  if s1==s2:
    return (True)
  else:
    return (False)







#проверка 9 значного пан цифрового
#числа
def pan_proverka(x):
  s = str(x)
  if len(s)!=9:
    return (False)
  if set("123456789") == set(s):
    return (True)
  else:
    return (False)







#число треугольное
def is_treug_chi(x):
  n = -0.5+(0.25+2*x)**0.5
  if (n - int(n)) != 0:
    return False
  else:
    return True







#Перебор/перестановка
n = 1000000
kol = 1
z = [0,1,2,3,4,5,6,7,8,9]


#z = [0,1,2,3]
x = []

i = 0
print(kol,z)
while True:  
  while (i < len(z)-1):
    if (z[len(z)-i-1] > z[len(z)-i-2]):
      ll = len(x)
      for k in range (0,ll):
        del x[0]
      for k in range (0,i+2):
        x.append(z[len(z)-i-2+k])
      x.sort()
      for k in range (0,len(x)):
        if (x[k] == z[len(z)-i-2]):
          z[len(z)-i-2] = x[k+1]
          del x[k+1]
          break
      for j in range(0,len(x)):
        z[len(z)-i-1+j] = x[j]
      kol += 1
      print(kol,z)
      #if kol==n+1:
        #break
      i = 0
    else:
      i += 1
      if len(x)==0:
        break
  break








'''
разложение на множители
razlozhenie(24)=[2,2,2,3]
'''
def razlozhenie(x):
  lst = []
  y = x
  while True:
    print(y)
    plus = False
    for j in range(2,int(y**0.5)+1):
      if (y%j == 0):
        y = y//j
        lst.append(j)
        plus = True
        break
    if not plus:
      break
  lst.append(y)
  return (lst)





#преобразование числа в список
def int_to_list(x):
  lst = []
  while x>0:
    lst.append(x%10)
    x //= 10
  lst.reverse()
  return(lst)




#preobrazovanie spiska v chislo
def list_to_int(x):
  y = 0
  for i in range(len(x)):
    y += x[i]*(10**(len(x)-i-1))
  return(y)





#количество знаков в числе
def int_kol(x):
  kol = 0
  while x>0:
    kol += 1
    x //= 10
  return(kol)







#Проверка числа на простоту, решетом
#global variabes
u = []
start_mas = 2

def is_prime(number):
  global u
  global start_mas
  mas = []

  if len(u) == 0:
    n_mas = number-1
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
    start_mas += n_mas    
    if mas[len(mas)-1]==0:
      return False
    else:
      return True

  n_mas = number-start_mas+1
  mas = []
  for i in range(0,n_mas):
    mas.append(start_mas+i)
  for i in range(len(u)):
    step = u[i][0]
    poz = u[i][1]
    poz += step
    while poz < start_mas+n_mas:
      mas[poz-start_mas] = 0
      poz += step
    u[i][1] = poz

    start_mas += n_mas    
    if mas[len(mas)-1]==0:
      return False
    else:
      return True
#print(is_prime(4))
#print(is_prime(28))
#print(is_prime(1001))
