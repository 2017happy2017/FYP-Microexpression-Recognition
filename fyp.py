#1-Extract each Frames from Video
#2-Detect emotion from every Frames
#3-Save emotions result
import argparse
import extract
import analyze

def main():
    parser = argparse.ArgumentParser(description='Testing')
    parser.add_argument('-r','--path',help='Extract frames from video')
    parser.add_argument("-detect", action='store_true', help="Detect emotion on each frames")
    args = parser.parse_args()
    extract.extractFrames(args.path)

    if args.detect:
        analyze.detectEmotion()


if __name__ == '__main__':
   main()
