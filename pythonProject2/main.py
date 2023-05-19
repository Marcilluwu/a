import random
import datetime
astolfo = datetime.datetime.now()
x =[1]
z = [1]
num = 100
y = 1
b = 0
while y != num+1:
   a = int(random.randrange(1,100))
   x.insert(y,a)
   y = y+1
y = 1
c = x
while not b > num:
   while y <= num - 1:
       if x[y] <= x[y + 1]:
           z.insert(y, x[y])
           z.insert(y + 1, x[y + 1])
           y = y + 2
       else:
           z.insert(y, x[y])
           z.insert(y, x[y + 1])
           y = y + 2
   y = 1
   z = z[1:]
   x = [1]
   while y < num - 1:
       if z[y] <= z[y + 1]:
           x.insert(y, z[y + 1])
           x.insert(y, z[y])
           y = y + 2
       else:
           x.insert(y, z[y])
           x.insert(y, z[y + 1])
           y = y + 2
   x.insert(num-1, z[num-1])
   x.insert(1, z[0])
   b = b+1
   y = 1
   z = [1]
while y <= num - 1:
       if x[y] <= x[y + 1]:
           z.insert(y, x[y])
           z.insert(y + 1, x[y + 1])
           y = y + 2
       else:
           z.insert(y, x[y])
           z.insert(y, x[y + 1])
           y = y + 2
print(z[1:])
print(datetime.datetime.now()-astolfo)