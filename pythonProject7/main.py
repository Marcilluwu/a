import datetime
import random
a = []
l = 0
for i in range(100001):
    a.append(random.randrange(1, 2139213213))
t1 = datetime.datetime.now()
for i in range(100001):
    l = l + a[i]
print(l)
tt4 = (datetime.datetime.now() - t1)
print(tt4)
t1 = datetime.datetime.now()
for i in range(100001):
    l = l - a[i]
print(l)
tt1 = (datetime.datetime.now() - t1)
print(tt1)
for i in range(100001):
    a.append(random.randrange(1, 2139213213))
t1 = datetime.datetime.now()
for i in range(100001):
    l = l * a[i]
print(l)
tt2 = (datetime.datetime.now() - t1)
print(tt2)
for i in range(100001):
    a.append(random.randrange(1, 2139213213))
t1 = datetime.datetime.now()
for i in range(100001):
    l = l / a[i]
print(l)
tt3 = (datetime.datetime.now() - t1)
print(tt3)
for i in range(100001):
    a.append(random.randrange(1, 2139213213))