# FYP-Microexpression-Recognition
Deepface is a lightweight face recognition and facial attribute analysis framework that developed by [Sefik Ilkin Serengil](http://https://github.com/serengil/deepface#face-recognition.com). My final project title is *Facial Micro-Expressions Recognition Based on Transfer Learning*. Transfer Learning is a machine learning method where a model is trained for a task is reused as the starting point for a model on task. Likewise, DeepFace framework already have a pre-trained model to detect macro-expressions that can be reused on micro-expressions recognition.

__Process of micro-expressions recognition:__
1. Extract every frames of a video into image format.
1. Detect emotion on each frame using DeepFace framework.
1. Every emotions detected will be saved in a folder.




### DeepFace Framework Installation

```python
pip install deepface
```

### Help Command
```python
python fyp.py -h
```

This command will display all other commands that available in this python script.

### Extract Frame From Video
```python
python fyp.py -r video.mp4
```
This command will extract every frames of a video and save into "Extracted Frame" folder. 




#### Sample Output
![](https://github.com/alvinlim99/FYP-Microexpression-Recognition/blob/main/icon/help.JPG)
