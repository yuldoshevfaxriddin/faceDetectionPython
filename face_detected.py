#  video fayldagi yuzlarni aniqlash
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)
face_cascade_db = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')


eyes_cascade_db = cv2.CascadeClassifier('cascades/haarcascade_eye_tree_eyeglasses.xml')



while True:
    succes ,img = cap.read()
    img = cv2.flip(img,2)
    # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(img,1.1,10)
    eyes = eyes_cascade_db.detectMultiScale(img,1.1,10)
#    print(type(faces))
#    print(len(faces))
#    print(type(img))
#    print(len(img))
    for (x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,"Yuzlar soni : {}".format(len(faces)),(10,40),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)
    cv2.imshow('window',img)
    # cv2.imshow('window2',img_gray)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
