import random
x =[0]
z = [0]
num = 15
y = 1
b = 0
d = [0]
while y != num+1:
   a = int(random.randrange(1,100))
   x.insert(y,a)
   y = y+1
y = 1
c = x
x = x[1:]
while b <= num - 1:
    print(x)
    z = min(x)
    print(z)
    d.insert(b + 1,z)
    x.remove(z)
    b = b+1
print(d[1:])