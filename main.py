import cv2
import numpy as np
import datetime
from ffpyplayer.player import MediaPlayer

vid = cv2.VideoCapture(0)
vid.set(3,1000)
vid.set(4,1000)
count = np.random.randint(0,100)
countstr = str(count)
while vid.isOpened():
    ret,frame = vid.read()
    if ret == True:
        g = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        text = str(datetime.datetime.now())
        # g = cv2.putText(g,text,(10,40),cv2.FONT_HERSHEY_TRIPLEX,1,(0,233,233),2)
        cv2.imshow('video',g)
        k = cv2.waitKey(15)
        if k==27:
            break
        elif k==ord(' '):
            str = "savedscreenshot"+countstr+".png"
            cv2.imwrite(str,g)
            e = cv2.imread(str,1)
            cv2.imshow(str,e)
            cv2.waitKey(0)
            break
    else:
        break
vid.release()
