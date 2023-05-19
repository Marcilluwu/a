import time
import random
f = open("palabras.txt")
a = (f.read())
no = 0

while True:
    b = ""
    np = a[1]
    b = input("Palabra ")
    c = int(len(b))
    if no == 1:
        no = 0
    for n in range(7455375):
        if b == a[n: n + c] and a[n-1] == np:
            print()
            print(chr(27) + "[0;39m", b)
            no = 1
            break
    if no == 0:
        print(chr(27) + "[0;32m", b, end=' ')