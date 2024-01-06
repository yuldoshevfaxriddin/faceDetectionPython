
import cv2 as cv
import time
import math

BLUE = (255,0,0)
GREEN = (0,255,0)
RED = (0,0,255)
path = 'cascades/haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)

cap = cv.VideoCapture(0)
TEMP_COLOR = RED 
print('boshlandi')
#print(face_detector)

while True:
    _,image = cap.read()
        
    face_rects=face_detector.detectMultiScale(image,scaleFactor=1.1)
    for rect in face_rects:
        #cv.rectangle(gray,rect,TEMP_COLOR,2)
        cv.rectangle(image,rect,TEMP_COLOR,2)
    cv.putText(image,"Yuzlar soni : {}".format(len(face_rects)),(10,60),cv.FONT_HERSHEY_SIMPLEX, 1,RED,2)
    cv.imshow('image',image)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
          break
cap.release()
cv.destroyAllWindows()






