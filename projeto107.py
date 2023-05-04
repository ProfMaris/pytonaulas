inferior = int(input("Numero Inferior  "))
superior = int(input("Numero Superior "))
divisao = int(input("Divisao "))

for num in range(inferior,superior):
    if (num%divisao==0):
        print(" Numero ",num)