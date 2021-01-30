import argparse
import os
import cv2

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

def main():
    parser = argparse.ArgumentParser(description='Testing')
    parser.add_argument('-r','--path',help='Extract frames from video')

    args = parser.parse_args()

    extractFrames(args.path)



if __name__ == '__main__':
   main()
