import cv2 as cv
import os

images = os.listdir(os.path.abspath('images'))

path = 'cascades/haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)
'''
f = open("tests.txt", "r")
tests = f.read()
tests = list(tests)
'''

#tests = [50,20,6,1,8,10,1,1,1,1,1,1]
tests = [50,1,1,1,20,6,1,8,10,1,1,1]

TEMP_COLOR = (255,0,0)
avg = 0
print('{} ta rasm '.format(len(tests)))
for index,i in enumerate(images):
    
    image = cv.imread('images/{}'.format(i))
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #cv.imshow('gray',gray)
    
    face_rects=face_detector.detectMultiScale(gray,scaleFactor=1.2)
    for rect in face_rects:
        cv.rectangle(image,rect,TEMP_COLOR,2)
    
    if len(face_rects)>tests[index]:
        foiz = len(face_rects)/(tests[index])*100 - 100
        print('xatolik :','{}/{} = {} %'.format(len(face_rects),tests[index],foiz))
    else :
        foiz = len(face_rects)/tests[index]*100
        print('{}/{} = {} %'.format(len(face_rects),tests[index],foiz))
    
    
    #print('{}/{} = {} %'.format(len(face_rects),tests[index],(len(face_rects)/tests[index]*100)))
    #cv.putText(image,"Yuzlar soni : {}".format(len(face_rects)),(10,60),cv.FONT_HERSHEY_SIMPLEX, 1,RED,2)
    avg += len(face_rects)/tests[index]*100
    cv.imshow('image',image)
    cv.waitKey(0)
    
print('O`rtacha : {}'.format(avg/len(tests)))    
cv.destroyAllWindows()



