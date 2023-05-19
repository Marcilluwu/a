import time
import random

def generar_palabras():
    Consonantes1 = ""
    Vocales1 = ""
    Consonantes2 = ""
    Vocales2 = ""
    Consonantes3 = ""
    Vocales3 = ""
    Consonantes4 = ""
    Vocales4 = ""
    Consonantes5 = ""
    Vocales5 = ""
    Consonantes6 = ""
    Vocales6 = ""
    Consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x",
                   "y", "z", "ñ"]
    Vocales = ["a", "e", "i", "o", "u"]
    silabas = random.randrange(1, 6)
    for i in range(random.randrange(1, 3)):
        Consonantes1 = Consonantes1 + Consonantes[random.randrange(0, 20)]
    for i in range(random.randrange(1, 3)):
        Vocales1 = Vocales1 + Vocales[random.randrange(0, 4)]
    if silabas == 1:
        return Consonantes1 + Vocales1

    for i in range(random.randrange(1, 3)):
        Consonantes2 = Consonantes2 + Consonantes[random.randrange(0, 20)]
    for i in range(random.randrange(1, 3)):
        Vocales2 = Vocales2 + Vocales[random.randrange(0, 4)]
    if silabas == 2:
        return Consonantes1 + Vocales1 + Consonantes2 + Vocales2

    for i in range(random.randrange(1, 3)):
        Consonantes3 = Consonantes3 + Consonantes[random.randrange(0, 20)]
    for i in range(random.randrange(1, 3)):
        Vocales3 = Vocales3 + Vocales[random.randrange(0, 4)]
    if silabas == 3:
        return Consonantes1 + Vocales1 + Consonantes2 + Vocales2 + Consonantes3 + Vocales3

    for i in range(random.randrange(1, 3)):
        Consonantes4 = Consonantes4 + Consonantes[random.randrange(0, 20)]
    for i in range(random.randrange(1, 3)):
        Vocales4 = Vocales4 + Vocales[random.randrange(0, 4)]
    if silabas == 4:
        return Consonantes1 + Vocales1 + Consonantes2 + Vocales2 + Consonantes3 + Vocales3 + Consonantes4 + Vocales4

    for i in range(random.randrange(1, 3)):
        Consonantes5 = Consonantes5 + Consonantes[random.randrange(0, 20)]
    for i in range(random.randrange(1, 3)):
        Vocales5 = Vocales5 + Vocales[random.randrange(0, 4)]
    if silabas == 5:
        return Consonantes1 + Vocales1 + Consonantes2 + Vocales2 + Consonantes3 + Vocales3 + Consonantes4 + Vocales4 + Vocales5 + Consonantes5

    for i in range(random.randrange(1, 3)):
        Consonantes6 = Consonates6 + Consonantes[random.randrange(0, 20)]
    for i in range(random.randrange(1, 3)):
        Vocales6 = Vocales6 + Vocales[random.randrange(0, 4)]
    if silabas == 6:
        return Consonantes1 + Vocales1 + Consonantes2 + Vocales2 + Consonantes3 + Vocales3 + Consonantes4 + Vocales4 +  Consonantes5 + Vocales5 + Consonantes6 + Vocales6

print(chr(27) + "[0;32m", "", end='')
while True:
    b = ""
    b = generar_palabras()
    c = int(len(b))
    s = open("palabras (còpia).txt", "a")
    f = open("palabras.txt")
    a = (f.read())
    no = 0
    np = a[1]
    np2 = """
    """
    if no == 1:
        no = 0
    for n in range(7455375):
        if b == a[n: n + c] and a[n-1] == np and a[n+c] == np:
            print()
            print(chr(27) + "[0;39m", "")
            for n in range(len(b)):
                print(b[n:n + 1], end="")
                time.sleep(0.1)
            print("")
            no = 1
            s.write(b + np2)
    if no == 0:
        print(chr(27) + "[0;32m", "", end="")
        for n in range(len(b)):
            print(b[n:n + 1], end="")
            time.sleep(0.1)
        print("", end= " ")