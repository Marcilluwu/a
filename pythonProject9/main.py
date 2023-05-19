# codigo que falla
import time
import random
c = [10,9,8,7,6,5,4,3,2,1]
a = c.copy()
c.sort()
i = 0
num = 10
num1 = num
t1 = time.time()
for i in range(0,num):
    for k in range(0,num1):
        if a[k-1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
print(a)
b = c.copy()
print(b)
if a == b:
    print('bien')
else:
    print('no bien')
print(time.time()- t1)