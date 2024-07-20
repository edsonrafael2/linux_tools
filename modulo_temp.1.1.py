from time import sleep
import os

tmp = 0
contador = 0

def temporizador(contador):

    #contador = 0
    cont = 0
    os.system('clear')
    print("Wait for a seconds please ...")
    while True:
        sleep(1)
        cont +=1
        os.system('clear')
        print('Wait....',end=' ')
        print(f"{cont}%")
        print(contador)
        if contador > 0:
            break
    





temporizador(contador)
for i in range (15):
        sleep(1)
        tmp+= 1

if tmp > 10:
        contador = 1

print (contador)


