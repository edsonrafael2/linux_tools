import os
from time import sleep
import time
import subprocess



def menu():
    os.system('clear')
    print('ÃTENÇÃO!! Isso pode danificar seu Sistema Operacional.')
    print('ATENÇÃO!!!. Observe o menu, e tenha certeza de escolher os HDs antes de executar o programa!' )

    resp = int(input('''
        [1] Editar o arquivo disk_dd.sh, inserindo os HDs corretos. 
        [2] Verificação do HD.
        [3] Executar o programa.
        [4] Sair do programa:  '''))
    return resp
     
def temporizador(duracao):

    contador = 0
   
    os.system('clear')
    print("Wait for a seconds please ...")
    while contador < duracao:
        sleep(1)
        contador+=1
        os.system('clear')
        print('Wait....',end=' ')
        print(contador)
        print('tempo de espera concluido!!')
        
def editar_arquivo():
    os.system("vim disk_dd.sh")

def verificar():
    ver = int(input('''
            [1] Verificar com fdisk -l: 
            [2] Verificar com Gparted: '''))
    if ver == 1:
            os.system("sudo fdisk -l ")
    elif ver == 2:
            os.system("sudo gparted")
    
def executar():
    duracao = 1
    print("Iniciando a execução do script...")
    #start_time = time.time() 
    process = subprocess.Popen(["sudo", "./disk_dd.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return_code = process.wait()  # Espera até o processo terminar e captura o código de retorno
    #end_time = time.time()
    #duracao = end_time - start_time

    #while 1:
        #sleep(2) 
    if return_code == 0:
            print('Programa executado com sucesso!')
            print(f'ESTE É O VALOR DO CODIGO = {return_code}')
            #break
    else:
             duracao += 1
             #temporizador(int(duracao))
        #else:
        #    print(f'Programa terminou com erros. Código de retorno: {return_code}')
    
    print(f'Tempo de execução: {duracao:.2f} segundos')
    temporizador(int(duracao))
    print('Operação concluída!')#-> O tempo de duração sera feito na função. 

def main(): 

    while 1:
        
        resposta = menu()                
        if resposta == 1:
            editar_arquivo()

        elif resposta == 2:
            verificar()

        elif resposta == 3:
            executar()

        elif resposta == 4:
            break
        
    print('Fim do Programa!!!')

main()

        