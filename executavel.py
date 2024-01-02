import os
from time import sleep


        
while 1:
    print('ÃTENÇÃO!! Isso pode danificar seu Sistema Operacional.')
    print('ATENÇÃO!!!. Observe o menu, e tenha certeza de escolher os HDs antes de executar o programa!' )
    resp = int(input('''
        [1] Editar o arquivo disk_dd.sh, inserindo os HDs corretos. 
        [2] Verificação do HD.
        [3] Executar o programa.
        [4] Sair do programa:  '''))
    
    if resp == 1:
        os.system("vim disk_dd.sh")

    if resp == 2:
        ver = int(input('''
            [1] Verificar com fdisk -l: 
            [2] Verificar com Gparted: '''))
        if ver == 1:
            os.system("sudo fdisk -l ")
        elif ver == 2:
            os.system("sudo gparted")

    if resp == 3:
        print('Aguarde um momento......!')
        sleep(2)
        print()
        #os.system("sudo ./disk_dd.sh")
        print()
        print('Programa executado!!')

    if resp == 4:
         break
print()
print('Fim do Programa!!!')
