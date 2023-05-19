import random
x =[0]
z = [0]
num = 4
y = 1
b = 0
d = [0]
e = 1
sort = 0
numlist = 1
menor = 1
ordenados = [0]
numorden= 1
ord = 1
#while y != num+1:
#   a = int(input("números: "))
#   x.insert(y,a)
#   y = y+1
x = [0,4,3,2,1]
y = 1
c = x
x = x[1:]
ordenaciones = 0
while b <= num - 1:
    while e == 1:
           while ord == 1:
               if x[b] <= x[numlist]:
                   ordenaciones = ordenaciones + 1
                   print(x[b])
                   print(x[numlist])
                   numlist = numlist + 1
                   sort = sort + 1
               else:
                   print(x[b])
                   print(x[numlist])
                   menor = 0
                   sort = num
                   ord = 0
                   numlist = numlist + 1
                   ordenaciones = 0
           numlist = 1
           print("no")
           if menor == 1:
               ordenados.insert(numorden, x[b])
           b = b + 1
           ord = 1
print(d[1:])
