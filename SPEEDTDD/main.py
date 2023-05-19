#Cosa rara rápida

import random

def listacomprobar():
    Posicion,Lista,numero = Colocar()
    Lista.append(numero)
    Lista.sort()
    listaIndex = Lista.index(numero)
    if listaIndex != Posicion:
        print('Ésta mal colocada')
        return
    print("Ta bien")

def Colocar():
    lista, numero, rango = ListaValores()
    a = rango
    while True:
        if numero > lista[a]:
            a += 1
            print("debería de estar en la posición",a)
            return a,lista,numero
        if numero == lista[a]:
            a -= lista.count(numero)-1
            print("debería de estar en la posición",a)
            return a,lista,numero
        if numero < lista[a-1] and numero > lista[a]:
            print("debería de estar en la posición",a)
            return  a,lista,numero
        if a < 0:
            a = 0
            print("debería de estar en la posición",a)
            return a,lista,numero
        else:
            a -= 1
def ListaValores():
    lista = []
    rng = 20
    for i in range(rng):
        lista.append(random.randrange(1,rng))
    lista.sort()
    print(lista)
    numero = int(input('¿Que número quieres introducir? '))
    return lista, numero, rng-1

listacomprobar()