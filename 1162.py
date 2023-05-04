# instalar numpy
# pip3 install NumPy
# se  a versão do python estiver desatulizada atualizar
#   py -m pip install --upgrade pip
#
# imprimindo array
# mudando um intervalo de array de cor

import numpy
import cv2

# um quadro preto 
black = numpy.zeros([600,600])

#linha =black[1:5,:]
#print(linha)
#coluna =black[:,1:2]
#print(coluna)

##print(black)
# Final
black[200:400,200:400]=255
print(black)
cv2.imshow("preto",black)
cv2.waitKey(0)