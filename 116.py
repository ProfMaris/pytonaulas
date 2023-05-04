# pip3 install opencv-python
# importar um módulo
# atribui uma imagem para uma variavel

# array
# print o array de cores
# array /matriz de várias dimensões

# matriz1d=[]

# matriz2=[[][]]
# matriz2=
# 0. [["A","B"],[1,3]]
# 1. [["C","D"],[2,4]]
# 2. [["E","F"],[2,5]]

# matriz3=[[[][][]]]
# 0. [["A","B"],[1,3],["Amor","Beleza"]]
# 1. [["C","D"],[2,4],["Casa","Dedicação"]]
# 2. [["E","F"],[2,5],["Estrela"],["Fé"]]
# Acessar o primeiro element do primeiro array
# [[0][0][0]]
# Acessar o segundo elemento do terceiro array
# [[1][2][2]]

 #pip3 install NumPy
 #atualizar o py -m pip install --upgrade pip 

import cv2
img=cv2.imread("C://Users\\User\\Desktop\\imagens\\imagem_surf.jpg")
#print(img)
#cv2.imshow("Surf",img)
#cv2.waitKey(0)


img_cinza=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Image",img_cinza)
cv2.waitKey(0)