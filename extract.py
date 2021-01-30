import cv2
import os

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

def extractFrames(n):
    path = n
    #Read video from specified path
    cam = cv2.VideoCapture(path)
    try:

        # creating a folder named data
        if not os.path.exists('Extracted Frames'):
            os.makedirs('Extracted Frames')

    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')

    # frame
    currentframe = 0

    while(True):

        # reading from frame
        ret,frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './Extracted Frames/frame' + str(currentframe) + '.jpg'
            print ('Extracting...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1

            #Set Number of frame
            #if currentframe==30:
                #break
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
