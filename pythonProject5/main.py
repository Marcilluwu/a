# Código redundante
import random
import time
c = [10,9,8,7,6,5,4,3,2,1]
i = 0
num = 100
num1 = num
for i in range(1,num+1):
    c.append(int(random.randrange(1,100)))
a = c.copy()
c.sort()
t1 = time.time()
for i in range(1,num1):
    for k in range(1,num):
        if a[k-1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
print(a)
b = c.copy()
print(b)
if a == b:
    print('bien')
print(time.time() - t1)