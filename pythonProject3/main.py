import time
import random
global num
num = 0
def crear_lista(num):  # crear lista
    lista = []
    for i in range(1,num+1):
        lista.append(int(random.randrange(1,100)))
    return lista
def ordenar(lista):      # ordenar for
    num1 = num
    for i in range(1,num):
        for k in range(1,num1):
            if lista[k-1] > lista[k]:
                lista[k], lista[k - 1] = lista[k - 1], lista[k]
        num1 -= 1
    return lista
def comprobar():      #comprobar que la funcion ordenar ordena la lista
    lista = crear_lista(num)
    listaSort = lista.copy()
    listaSort.sort()
    listaPorComprobar = ordenar(lista)
    if listaSort == listaPorComprobar:
        return 'bien'
    else:
        return 'no bien'
num = int(input('cuantos números para ordenar '))
print(comprobar())