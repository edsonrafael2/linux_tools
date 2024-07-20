import os
import time
import subprocess
from time import sleep

def menu():
    os.system('clear')
    print('ATENÇÃO!! Isso pode danificar seu Sistema Operacional.')
    print('ATENÇÃO!!! Observe o menu, e tenha certeza de escolher os HDs antes de executar o programa!')

    resp = int(input('''
        [1] Editar o arquivo disk_dd.sh, inserindo os HDs corretos. 
        [2] Verificação do HD.
        [3] Executar o programa.
        [4] Sair do programa:  '''))
    return resp

def temporizador(duracao):
    contador = 0
    os.system('clear')
    print("Wait for a few seconds, please...")
    while contador < duracao:
        sleep(1)
        contador += 1
        os.system('clear')
        print('Wait....', end=' ')
        print(contador)
    print('Tempo de espera concluído!')

def editar_arquivo():
    os.system("vim disk_dd.sh")

def verificar():
    ver = int(input('''
            [1] Verificar com fdisk -l: 
            [2] Verificar com Gparted: '''))
    if ver == 1:
        os.system("sudo fdisk -l")
    elif ver == 2:
        os.system("sudo gparted")

def executar():
    print("Iniciando a execução do script...")
    start_time = time.time()
    
    process = subprocess.Popen(["sudo", "./disk_dd.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Captura da saída padrão e de erro
    while True:
        output = process.stdout.readline()
        error = process.stderr.readline()
        if output:
            print(output.strip())
        if error:
            print(error.strip())
        if output == '' and process.poll() is not None:
            break
    
    return_code = process.wait()  # Espera até o processo terminar e captura o código de retorno
    end_time = time.time()
    duracao = end_time - start_time
    
    if return_code == 0:
        print('Programa executado com sucesso!')
    else:
        print(f'Programa terminou com erros. Código de retorno: {return_code}')
    
    print(f'Tempo de execução: {duracao:.2f} segundos')
    temporizador(int(duracao))
    print('Operação concluída!')

def main(): 
    while True:
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
