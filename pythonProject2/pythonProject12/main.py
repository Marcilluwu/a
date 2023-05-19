import random
Consonantes = ["b","c","d","f","g","h","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z","ñ"]
print(chr(27) + "[0;32m", end='')
while True:
    for i in range(random.randrange(1,20)):
        print(end=' ')
    for i in range(random.randrange(1,3)):
        print(Consonantes[random.randrange(0,20)],end='')
    if 1 == random.randrange(1,25):
        print()