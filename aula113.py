#1.O módulo time fornece as funções para
#trabalhar com o tempo.
#2. O módulo OS do Python fornece funções
#para interagir com o sistema operacional.
#Ele vem com os módulos utilitários
#padrão do Python.
#3. O módulo Shutil oferece várias
#operações de alto nível em arquivos e
#coleções de arquivos
#Nas grandes empresas, um watchdog é uma
#pessoa ou grupo cujo trabalho é ficar de olho
#para garantir que as grandes empresas
#respeitem os direitos das pessoas.
#O Watchdog é uma API e um utilitário do Shell para monitorar eventos no arquivo de sistema. Em outras palavras, um diretório é passado como argumento para essa API que passa a ser observado pelo seu programa gerando alertas sobre eventos de criação, deleção, modificação e movimentação de arquivos e diretórios.
#Um programa simples que usa watchdog para monitorar diretórios especificados como argumentos de linha de comando e registra eventos gerados:
### instalar python -m pip install -U watchdog
### watchdog.observers.Observer é é a classe
   #que procurará qualquer alteração no
   #caminho fornecido. Ela chama o
   #gerenciador de eventos específico com
   #base nas alterações.
###watchdog.events.FileSystemEventHandler
   # é a classe do gerenciador de eventos
   #que irá gerenciar os eventos do sistema de
   #arquivos (como criação, modificação,
   #movimentação e exclusão de arquivos)


import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\\Users\\CLIENTES\\Downloads"              # Adicione o caminho da sua pasta "Downloads".
to_dir = "C:\\Users\\User\\Desktop\\imagens" # Crie a pasta "Arquivos_Documentos" em sua área de trabalho e atualize o caminho de acordo.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
  
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Baixado " + file_name)

                path1 = from_dir + '\\' + file_name
                path2 = to_dir + '\\' + key
                path3 = to_dir + '\\' + key + '\\' + file_name

                if os.path.exists(path2):

                    print("Diretório Existe...")
                    print("Movendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Criando Diretório...")
                    os.makedirs(path2)
                    print("Movendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Inicialize a Classe Gerenciadora de Eventos
evento = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(evento, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()