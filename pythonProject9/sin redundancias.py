# codigo con menos redundancias
import time
import random
c = [10,9,8,7,6,5,4,3,2,1]
a = c.copy()
i = 0
num = 10
num1 = num
t1 = time.time()
for i in range(1,num):
    for k in range(1,num1):
        if a[k-1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
    num1 -= 1
print(a)
c.sort()
b = c.copy()
print(b)
if a == b:
    print('bien')
print(time.time()- t1)