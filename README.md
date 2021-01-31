# FYP-Microexpression-Recognition
Deepface is a lightweight face recognition and facial attribute analysis framework that developed by [Sefik Ilkin Serengil](http://https://github.com/serengil/deepface#face-recognition.com). Final project title: *Facial Micro-Expressions Recognition Based on Transfer Learning*. Transfer Learning is a machine learning method where a model is trained for a task is reused as the starting point for a model on other task.DeepFace framework already have a pre-trained model to detect macro-expressions that can be reused on micro-expressions recognition.

__Process of micro-expressions recognition:__
1. Extract every frames of a video into image format.
1. Detect emotion on each frame using DeepFace framework.
1. Every detected emotions will be saved in a folder.

__#There's no function to automatically detect micro-expressions, required manually look throught all the detected emotions images to find any micro-expressions#__



### DeepFace Framework Installation

```python
pip install deepface
```

### Help Command
```python
python fyp.py -h
```
This command will display all other commands that available in this python script.

### Frames Extraction
```python
python fyp.py -r video.mp4
```
This command will extract every frames of a video and save into "Extracted Frame" folder. 

### Emotion Detection
```python
python fyp.py -detect
```
This command will detect emotions on every frames and save it into "Analyzed" Folder


### Testing
1. Extract every frames from a video.
    ![](https://github.com/alvinlim99/FYP-Microexpression-Recognition/blob/main/icon/1.JPG)
    ![](https://github.com/alvinlim99/FYP-Microexpression-Recognition/blob/main/icon/2.JPG)
1. Detect emotions on every extracted frames.
    ![](https://github.com/alvinlim99/FYP-Microexpression-Recognition/blob/main/icon/3.JPG)

#### Sample Output
Example of frame0 which is the first frame before and after emotions detection
![GitHub Logo](https://github.com/alvinlim99/FYP-Microexpression-Recognition/blob/main/Extracted%20Frames/frame0.jpg)
![](https://github.com/alvinlim99/FYP-Microexpression-Recognition/blob/main/Analyzed/analyzed_0.jpg)

### Acknowledgments
Implementations use the source code from following repositories and links:
* [Sefik Ilkin Serengil](https://github.com/serengil/deepface). 
* [GeeksforGeeks](https://www.geeksforgeeks.org/extract-images-from-video-in-python/)
