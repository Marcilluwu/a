import random
x =[]
y = 0
alfonso = 0
num = int(input("númoros a ordenar: "))
while y != num:
   x.insert(2,int(random.randrange(1,num * 2)))
   y = y+1
   alfonso = alfonso + 1
   print(alfonso)
j = 0
k = num-1
while not j == num - 1:
    while k != j:
        if x[k] < x[k-1]:
            x[k],x[k-1]=x[k-1],x[k]
        k = k - 1
        alfonso = alfonso + 1
        print(alfonso)
    k = num-1
    j = j+1
print(x)