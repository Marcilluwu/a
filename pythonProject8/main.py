import random     #Juego
z = 0
y = str('y')
x = str('y')
def num(c):       #Dar numero
    global b
    b = int(random.randrange(0,c+1))
def comprobar(a): #Tdd comprobar
    global b
    global z
    if a == b:
        print('yes',end=', ')
        z = 1
    if a > b:
        print('minus')
    if a < b:
        print('more')




print("""





Answer the number with 10 attempts!!


_____________________________________________________________________________________________________________________________________________


""")
while x == y:    #bucle
    z = 0
    num(int(input('from 0 until ')))
    for i in range(1, 12):
        comprobar(int(input('number: ')))
        print(f'attempt number {i}')
        print(i)
        if z == 1:        #acierto
            break
        if i == 10:       #fallo
            print('u lose')
            break
    print(f'the number was {b}')
    print('retry?')
    x = str(input('y/n? '))