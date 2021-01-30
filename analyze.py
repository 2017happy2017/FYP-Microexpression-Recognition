import cv2
from deepface import DeepFace
import os
import warnings
warnings.filterwarnings("ignore")



def draw():
    #Draw Rectangle on Face
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)



    #Write Emotion on Image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,
               predictions['dominant_emotion'],
               (400,200),
               font, 2,
               (0, 0, 255),
               2,
               cv2.LINE_4
           ) ;


def detectEmotion():
    list = os.listdir('Extracted Frames')
    number_files = len(list)

    for x in range(number_files):
        #count

        #Analyze Image
        warnings.filterwarnings("ignore")
        img = cv2.imread('Extracted Frames/frame'+ str(x) +'.jpg')
        predictions = DeepFace.analyze(img)
        warnings.filterwarnings("ignore")

        #draw
        #Draw Rectangle on Face
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)



        #Write Emotion on Image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,
                   predictions['dominant_emotion'],
                   (400,200),
                   font, 2,
                   (0, 0, 255),
                   2,
                   cv2.LINE_4
               ) ;


        cv2.imwrite('Analyzed/analyzed_'+ str(x) +'.jpg', img)
        print("Frame "+str(x)+ " Emotion Detected \n")
