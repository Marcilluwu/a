import random
import time

Consonantes = ["b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z","ñ"]
Vocales =     ["a","e","i","o","u"]
Signos = [";",":",".","/","%"]
print(chr(27) + "[0;32m" + "-/", end=' ')
while True:
    if 1 == random.randrange(0,15):
        print(Signos[random.randrange(1,5)], end = '')
    for i in range(random.randrange(1,6)):
        for i in range(random.randrange(1, 2)):
            print(Consonantes[random.randrange(1, 21)], end='')
        print(Vocales[random.randrange(0, 4)], end='')
    if 1 == random.randrange(0,15):
        print(end=' ')
        for i in range(1,7):
            print(random.randrange(0,9), end='')
        print(end=' ')
    if 1 == random.randrange(0,10):
        print(Signos[random.randrange(1,5)])
        if 1 == random.randrange(0, 10):
            print()
        print("-/",end=' ')
    else:
        print(end=' ')
    time.sleep(0.1)