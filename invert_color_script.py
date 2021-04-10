import os, cv2

for i in os.listdir('train'):
    for j in os.listdir('train/'+i):
        image = cv2.imread('train/'+i+'/'+j, 0)
        imagem = (255-image)
        ret,thresh1 = cv2.threshold(imagem,127,255,cv2.THRESH_BINARY)
        cv2.imwrite('train/'+i+'/'+j, imagem)
        
    