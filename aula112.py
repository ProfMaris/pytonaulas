# objetivo : ler os arquivos de um diretorio e  mover os arquivos com um determinada extensão para outra pasta existente.

# importar
import os
import shutil

# ver diretorio os.getcwd()
# listar todos os arquivos existentes os.listdir()
dir_origem="C:\\Users\\User\\Desktop\\python"
dir_destino="C:\\Users\\User\\Desktop\\python\\112"
dir_destino_sempasta="C:\\Users\\User\\Desktop\\python\\112e"
# qualquer diretorio
qualquer_diretorio = "C:\\Users\\User\\Downloads"
lista_arq = os.listdir(qualquer_diretorio)
#print(lista_arq)
# fazer a leitura de quaquer_diretorio e colocar no dir de origem
dir_origem = qualquer_diretorio

# listar todos os arquivos do diretorio com  suas extenções
# repetição 
# for ---- in.... :

if os.path.exists(dir_destino_sempasta): 
        
    for nome_arquivo in lista_arq:
        nome,ext = os.path.splitext(nome_arquivo)
        ## print("Nome arquivo ", nome)
        ## print("Extensão ", ext)
        if ext=='':
            continue
        if ext in ['.gif','.png','.jpg','.jpeg']:
            print("Fazendo copy para "+dir_destino)
            path1=dir_origem+"\\"+nome_arquivo 
            print(path1)
            path2=dir_destino+"\\"+nome_arquivo
            print(path2)
            shutil.copy(path1,path2)
            ## pode usar o shutil.move
else:
                
    print("Criando pasta "+dir_destino_sempasta)
    os.makedirs(dir_destino_sempasta) 
    dir_destino=dir_destino_sempasta