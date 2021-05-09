import cv2
import difflib
import os
 
files = os.listdir() 
images = list(filter(lambda x: x.endswith('.jpg'), files))
count=0
a=0
c=110000
#if c>10:
name=input("Название фотографий:")
images.remove(name)
#Функция вычисления хэша
while c>44:
    def CalcImageHash(FileName):
        image = cv2.imread(FileName) #Прочитаем картинку
        resized = cv2.resize(image, (15,15), interpolation = cv2.INTER_AREA) #Уменьшим картинку
        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #Переведем в черно-белый формат
        avg=gray_image.mean() #Среднее значение пикселя
        ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) #Бинаризация по порогу
    
    #Рассчитаем хэш
        _hash=""
        for x in range(15):
            for y in range(15):
                val=threshold_image[x,y]
                if val==255:
                    _hash=_hash+"1"
                else:
                    _hash=_hash+"0"
            
        return _hash
 
    def CompareHash(hash1,hash2):
        l=len(hash1)
        i=0
        count=0
        while i<l:
            if hash1[i]!=hash2[i]:
                count=count+1
            i=i+1
        return count
    a+=1
    b=images[count]
    hash1=CalcImageHash(name)
    hash2=CalcImageHash(b)
    print(hash1)
    print(hash2)
    c=CompareHash(hash1, hash2)
    print(c)
    print(b)
    if count< len(images):
        count+=1
print(b+ " и " + name + " чем-то похожи")
input("")