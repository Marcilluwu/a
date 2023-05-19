import random
def comprobar():
    NumeroEntrada,NumeroAAdivinar,Contador,IntentosTotales,Perdido = juego()
    if NumeroEntrada == NumeroAAdivinar and Contador == IntentosTotales and Perdido == 1:
        print('No ha comprobado bien')
        return
    if NumeroEntrada != NumeroAAdivinar and Contador != IntentosTotales:
        print('No ha acabado cuando debía')
        return
    print('todo bien')

def juego(): #Comprueba si A es major, menor o igual a B en caso de que los intentos sean favorables
    Contador = 0
    Perdido = 0
    Rango = 1000
    IntentosTotales = 10
    NumeroAAdivinar = random.randrange(1, Rango)
    print(NumeroAAdivinar)
    print("Adivina un número del 1 al 1000 en 10 intentos")
    while Perdido == 0:
        NumeroEntrada = int(input('Número: '))
        print('Intento nº', Contador+1)
        if Contador == IntentosTotales:
            print('has perdido')
            Perdido = 1
            break
        if NumeroEntrada == NumeroAAdivinar:
            print('el número introducido es correcto')
            break
        if NumeroEntrada < NumeroAAdivinar:
            print('El número a adivinar es mayor')
        if NumeroEntrada > NumeroAAdivinar:
            print('El número a adivinar es menor')
            Contador += 1
    return NumeroEntrada,NumeroAAdivinar,Contador,IntentosTotales,Perdido

#_________________________________________________Programa________________________________________________
y = str('y')
n = str('n')
while True:
    comprobar()
    continuum = 1
    while continuum != y:
        continuum = str(input('Volver a jugar? (y/n) '))
        if continuum == n:
            print('Adiós')
            exit(0)