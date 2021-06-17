import cv2
from imutils.video import WebcamVideoStream
import os
print(__file__[:-9])

#WebCamVideoStream will take images form the camera

class VideoCamera(object):
    def __init__(self):

        # initializing webcam
        # src will depend on your system
        # start will turn on your camera
        self.stream=WebcamVideoStream(src=0).start()
    
    def __del__(self):


        #to stop the camera
        self.stream.stop()

    def get_frame(self):
        # collecting the image
        image=self.stream.read()

        # path to the folder
        path=__file__[0:-9]
        new_path=path+"haarcascade_frontalface_default.xml"
        
        # creating the detector
        detector=cv2.CascadeClassifier(new_path)

        # parameters --> image passed,threshold,neighbours
        face=detector.detectMultiScale(image,1.1,7)

        #loop for multifaces
        for(x,y,h,w) in face:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

        ret,jpeg=cv2.imencode('.jpg',image)
        data=[]
        #image is stored in bytes
        data.append(jpeg.tobytes())
        return data