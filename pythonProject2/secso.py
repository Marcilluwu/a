#menú
import datetime
import random
import math
import datetime
import random
import time
looping = 0
d = []    #variaciones de la lista
a = []    #variaciones de la lista
s = []    #variaciones de la lista
b = []    #variaciones de la lista
t = []    #variaciones de la lista
l = 0     #Control de loops
i = 0     #Control de loops
sd100 = []#lista específica
ñoclo = []#lista específica
def mushascoshas():                      #comparar 100000 operaciones
    print('suma')
    l = 0     #salida numerica
    a = 0     #salvavidas
    for i in range(100001):
        sd100.append(random.randrange(1, 9))    #lista
    t1 = time.time()
    for i in range(100001):
        l = l + sd100[i]
    tt1 = (time.time() - t1)
    print(l)
    print(tt1)
    input('Pulsa para pasar al siguiente')
    print('resta')
    t1 = time.time()
    l = 0
    for i in range(100001):
        l = l - sd100[i]
    tt2 = (time.time() - t1)
    print(l)
    print(tt2)
    input('Pulsa para pasar al siguiente')
    print('multiplicacion')
    t1 = time.time()
    l = 1
    for i in range(100001):
        l = sd100[i-1] * sd100[i]
    tt3 = (time.time() - t1)
    print(tt3)
    print(l)
    input('Pulsa para pasar al siguiente')
    print('división')
    t1 = time.time()
    l = sd100[i]
    for i in range(100000):
        l = l / sd100[i + 1]
    tt4 = (time.time() - t1)
    print(l)
    print(tt4)
    input('Pulsa para pasar al siguiente')
    t1 = time.time()
    l = sd100[i]
    print('comparación')
    for i in range(100000):
        if sd100[i] < sd100[i + 1]:
            a += 1
        else:
            a += 1
    tt5 = (time.time() - t1)
    print(tt5)
    ñoclo = [tt1, tt2, tt3, tt4, tt5]
    ñoclo.sort()
    input('Pulsa para pasar al siguiente')
    print("De mayor a menor", ñoclo)
    ttt1 = ((tt1 + tt2 + tt3 + tt4 + tt5) / 5)
    print('media', ttt1)
    print('diferencia resta y la media')
    print(tt1 - ttt1)
    print('diferencia suma y la media')
    print(tt2 - ttt1)
    print('diferencia multiplicación y la media')
    print(tt3 - ttt1)
    print('diferencia división y la media')
    print(tt4 - ttt1)
    print('diferencia comparar y la media')
    print(tt5 - ttt1)
    print('Cuantas veces mas tarda restar en comparacion con sumar')
    print(tt2 / tt1)
    print('Cuantas veces mas tarda multiplicar en comparacion con sumar')
    print(tt3 / tt1)
    print('Cuantas veces mas tarda dividir en comparacion con sumar')
    print(tt4 / tt1)
    print('Cuantas veces mas tarda comparar en comparacion con sumar')
    print(tt5 / tt1)
    input('Pulsa para volver al menú')
def barra():                                                #barra salida
    Largo = 138
    Total = 10
    Total1 = int(Total+1)
    p = str()      #caracter vacio salvavidas
    for Cargado in range(Total1):
        Porcentaje = float(Cargado / Total)
        imprimible = str(Cargado)
        parte1 = int(Largo * Porcentaje)
        parte2 = int(Largo - parte1)
        print("""









        """)
        print(chr(27)+"[0;32m"+p.rjust(parte1, '#'), end='')
        print(chr(27)+"[3;37m"+p.ljust(parte2, '·'), end=' ')
        print(int(Porcentaje * 100), "%")
        time.sleep(5/Total)
def sortear():                                  #ordenar por sort para comparar
    t = s.copy()
    print(t)
    t.sort()
    print(t)
def comprobar(d):                               #compporbar
    b = s.copy()
    if d == b:
        print('bien')
    else:
        print('no bien')
def ordfor():                                   #ordenar con for
    sdf = s.copy()
    i = 0
    num = 100
    num1 = num
    for i in range(1, num):
        for k in range(1, num1):
            if sdf[k - 1] > sdf[k]:
                sdf[k], sdf[k - 1] = sdf[k - 1], sdf[k]
        num1 -= 1
    print(a)

def cien():                                      #ordenar burbuja
    j = 0
    k = 99
    b = s.copy()
    print(b)
    while j != 100:
        while k != j:
            if b[k] < b[k - 1]:
                b[k], b[k - 1] = b[k - 1], b[k]
            k -= 1
        j += 1
        k = 99
    print(b)


def cienn():                                      #ordenar burbuja para comparar
    a = []
    i = 0
    while i != 100:
        a.append(int(random.randrange(100)))
        i += 1
    j = 0
    k = 99
    while j != 100:
        while k != j:
            if a[k] < a[k - 1]:
                a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1
        j += 1
        k = 99
    print(a)
    input('Pulsa para volver al menú')
def conpra():                                        #lista de la compra
    y = 0
    x = 0
    Numero_art = 3
    Chicles = 0.5
    Pan = 0.9
    Chocolate = 1.5
    while (x > Numero_art or x == 0):
        print(""""'Tipo Articulo
        0) Lista de Articulos
        1) Chicles 0.5 euros
        2) Pan 0.9 euros
        3) Chocolate 1.5 euros'""")
        x = int(input('Elije: '))
        if x > Numero_art:
            print('Argumento Invalido')
            print('____________________________________________________')
    if x == 1:
        y = Chicles
    if x == 2:
        y = Pan
    if x == 3:
        y = Chocolate
    z = int(input('cantidad '))
    print('A pagar: ', z * y, 'euros')
    input('Pulsa para volver al menú')
def tresnum():                                  #ordenar tres números
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    c = int(input('tercer numero: '))
    if a >= b and a >= c:
        if b >= c:
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        if b >= a and b >= c:
            if a >= c:
                print(b, a, c)
            else:
                print(b, c, a)
        else:
            if b >= a:
                print(c, b, a)
            else:
                print(c, a, b)
    input('Pulsa para volver al menú')
def sorteado():                                          #ordenar por sort
    a= []
    i = 0
    while i != 100:
        a.append(int(random.randrange(100)))
        i += 1
    a.sort
    print(a)
    input('Pulsa para volver al menú')
def caida():                                             #tiempo en caer
    Vo = float(input('Velocidad inicial: '))
    print(2*Vo/9.8)
    input('Pulsa para volver al menú')
def sqrt():                                              #area quadrado
    l = float(input('Lado: '))
    print(l*l)
    input('Pulsa para volver al menú')
def Jueguito():                                          #Juego adivinar número
    Número = random.randrange(1,100)
    x = 7
    print('Adivine un número del 1 al 100, tiene',x, 'intentos')
    for i in range(1,x+1):
        if i != 1:
            print('intento número', i)
        y = int(input('Número: '))
        if i ==  x:
            print('Has perdido, el número era',Número)
            break
        if y == Número:
            print('Has ganado')
            break
        if y > Número:
            print('El número es menor')
        if y < Número:
            print('El número es mayor')
    input('Pulsa para volver al menú')
for i in range(100):
    s.append(random.randrange(1, 100))
b = s
t = s
while True:                                              #menú
    print(""""'Operacion:
    1) Ordenar 100 números aleatorios burbuja
    2) Precio compra
    3) Ordenar 3 números dados
    4) Ordenar 100 números sort
    5) Calcular caída
    6) Area cuadrado
    7) Lista pregenerada y ordenar, diferencia de tiempos
    8) Comparación 100000 operaciones
    9) Adivinar un número del 1 al 100
    10) Salir
    //Para comprobar la diferencia entre ordenar 100 números con burbuja y con sort, use los dos comandos seguidos//'""")
    x = int(input('Elije: '))
    if not x <= 10 and x >= 1:                      #Argumento invalido
        print(""""'Argumento Invalido'
        ____________________________________________________'""")
    if x == 1:                                              #ordenar 100 números
        t1 = datetime.datetime.now()
        cienn()
        tt2 = datetime.datetime.now() - t1
        print(tt2)
    if x == 2:                                              #lista de la compra
        conpra()
    if x == 3:                                              #ordenar 3 números
        tresnum()
    if x == 4:                                              #sort
        t1 = datetime.datetime.now()
        sorteado()
        tt3 = datetime.datetime.now()-t1
        print(tt3)
    if x == 5:                                              #T. Caida
        caida()
    if x == 6:                                              #A. cuadrado
        sqrt()
    if x == 7:                                              #comparar
        i = 0
        ttt1 = datetime.datetime.now()
        cien()
        tttt1 = datetime.datetime.now()-ttt1
        ttt2 = datetime.datetime.now()
        sortear()
        tttt2 = datetime.datetime.now() - ttt2
        ttt3 =datetime.datetime.now()
        ordfor()
        tttt3 = datetime.datetime.now() - ttt3
        print('while: ',tttt1)
        print('sort: ',tttt2)
        print('for:', tttt3)
        print('Cuantas veces mas tarda el algoritmo de burbuja con whiles que el sort: ',tttt1/tttt2)
        print('Cuantas veces mas tarda el algoritmo de burbuja con for que el sort: ', tttt3 / tttt2)
        print('Cuantas veces mas tarda el algoritmo de burbuja con whiles que el algoritmo de burbuja con for: ', tttt1 / tttt3)
        exit(0)
    if x == 8:                                   #operaciones
        mushascoshas()

    if x == 9:                                   #jueguito
        Jueguito()
    if x == 10:                                  #salir
        break
    looping += 1
    d.append(x)
    d.sort()
    if d == [1,4]:
        print('burbuja: ',tt2)
        print('sort: ',tt3)
        print('diferencia')
        print(tt2/tt3)
        exit
print("Saliendo del menu:")
time.sleep(1)
barra()
print("""
Adiós :)""")
exit(0)
