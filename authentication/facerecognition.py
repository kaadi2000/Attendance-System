from gui import loginscreen
import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

font = cv2.FONT_HERSHEY_SIMPLEX

def login():
    loginscreen.login_attendance()

def facerecognition(mode, user, pswd, detail):
    pass

def detect():
    recognizer.read('trainer/trained.yml')
    
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            if (confidence < 100):
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('Face Detection(Press ESC to close)',img) 

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break


    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
