import random
import time

def listacomprobar():
    Posicion,Lista,numero = Colocar()
    Lista1 = Lista.copy()
    Lista2 = Lista1.copy()
    Lista.append(numero)
    Lista.sort()
    Lista2.sort()
    if Lista1 != Lista2:
        return "No Está Ordenado"
    if len(Lista1) < 1001:
        return "Faltan Números"
    if len(Lista1) > 1001:
        return "Sobran Números"
    for i in range(Lista.count(numero)):
        if Posicion == (Lista.index(numero)+i) and Lista[Posicion] != Lista[(Lista.index(numero)+i)]:
            return "Está mal colocado"
    return "Está Bien"
def Colocar():
    lista, numero, rango = ListaGenerar()
    lista1 = lista.copy()
    lista.append(numero)
    lista.sort()
    numero1 = numero
    if numero > 10000:
        numero1 = 10001
    der = rango
    izq = 0
    med = int((der + izq + 1) * (numero1/10000))
    while True:
        if numero == lista[med]:
            print("debería de estar en la posición",med)
            return med, lista, numero
        if numero < lista1[med]:
            der = med-1
        if numero > lista1[med]:
            izq = med+1
        med = int((der + izq + 1) / 2)

def ListaGenerar():
    lista = []
    for i in range(1000):
        lista.append(random.randrange(1,10000))
    lista.sort()
    print(lista)
    numero = int(input('¿Que número quieres introducir? '))
    return lista, numero, 999

y = str('y')
n = str('n')
while True:
    print(listacomprobar())
    continuum = 1
    while continuum != y:
        continuum = str(input('Volver a usar? (y/n) '))
        if continuum == n:
            print('Adiós')
            exit(0)