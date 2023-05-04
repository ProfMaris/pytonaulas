import time

# programa
# obter um dado na tela
segs = input("Informe uma quantidade de segundos ");

# criar uma função para transformar os segundos em minutos e o resto de segundos.

def transtime(segs):
    mins = int(segs / 60)
    secs = int(segs % 60)

    timer =f'{mins}:{secs}'
    print(timer)
# chamar 
transtime(int(segs))