from tkinter import *
from tkinter import filedialog
from tkinter.font import ITALIC
import cv2, numpy, os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")

def selectfolder(id):
    temp = Tk()
    temp.withdraw()
    path = filedialog.askdirectory()

    def getImagesAndLabels(path):
        imagePaths = os.listdir(path)  
        faceSamples=[]
        ids = []

        for imagePath in imagePaths:
            temp = path + "/" + imagePath
            PIL_img = Image.open(temp).convert('L')
            img_numpy = numpy.array(PIL_img,'uint8')

            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids
    
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, numpy.array(ids))
    recognizer.write('trainer/trained.yml')


def camera(id):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    count = 0

    while(True):
        ret, img = cam.read()
        faces = detector.detectMultiScale(img, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            cv2.imwrite("trainer/cache/user." + str(id) + '.' + str(count) + ".jpg", img)

        cv2.imshow('Train', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
            break
    cv2.destroyAllWindows()

    def getImagesAndLabels(path):
        imagePaths = os.listdir(path)  
        faceSamples=[]
        ids = []

        for imagePath in imagePaths:
            temp = path + "/" + imagePath
            PIL_img = Image.open(temp).convert('L')
            img_numpy = numpy.array(PIL_img,'uint8')

            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids

    face_array, ids = getImagesAndLabels("trainer/cache")
    recognizer.train(face_array, numpy.array(ids))
    recognizer.write('trainer/trained.yml')

    for f in os.listdir('trainer/cache'):
        os.remove(os.path.join('trainer/cache', f))
