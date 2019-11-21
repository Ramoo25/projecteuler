import time

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

start_time = time.time()

mx = 1
x = 999
while (x > 100):
    y = x
    while (y>100) and (y > mx//x):
        if is_palindrome(x*y):
            if x*y>mx:
                mx = x*y
        y -= 1
    x -= 1
    
print("answer: ",mx)
print(time.time()-start_time)
