import random


resposta="y"
while (resposta=="y"):

    #numaleatorio
    no=random.randint(1,6)
    if no==1:
       print("[     ]")
       print("[     ]")
       print("[--0--]")
       print("[     ]")
       print("[     ]")
       print("[     ]")
    if no==2:
       print("[     ]")
       print("[  0  ]")
       print("[     ]")
       print("[  0  ]")
       print("[     ]")
       print("[     ]]")
    if no==3:
       print("[-----]")
       print("[-----]")
       print("[-----]")
       print("[0 0 0]")
       print("[-----]")
       print("[-----]")
    if no==4:
       print("[-----]")
       print("[0   0]")
       print("[-----]")
       print("[-----]")
       print("[0   0]")
       print("[-----]")
    if no==5:
       print("[-----]")
       print("[0---0]")
       print("[-----]")
       print("[--0--]")
       print("[-----]")
       print("[0---0]")
    if no==6:
       print("[-----]")
       print("[0---0]")
       print("[-----]")
       print("[0---0]")
       print("[-----]")
       print("[0---0]")
       
    resposta = input("Quer jogar um dado ?")
