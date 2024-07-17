import os
from time import sleep



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
    print('Aguarde um momento......!')
    sleep(2)
    print()
    #os.system("sudo ./disk_dd.sh")
    print()
    print('Programa executado!!')

def main():
        

    while 1:
        
        resposta = menu()
                
        if resposta == 1:
            editar_arquivo()

        elif resposta == 2:
            verificar()

        elif resposta == 3:
            executar()

        if resposta == 4:
            break
    print()
    print('Fim do Programa!!!')

main()

        