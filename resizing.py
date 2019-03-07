import cv2
import os
import numpy as np

imageformat = ".jpg"
path = '/home/vijesh/images-vis/480*360/img/ls/'
imfilelist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(imageformat)]
for el in imfilelist:
    img = cv2.imread(el)
    os.chdir('/home/vijesh')  # head region

    resiz = cv2.resize(img, (1360, 765))
    cv2.imwrite(str(el) , resiz)
    cv2.imshow('frame', resiz)
    #cv2.waitKey(30)


# print 'staring frames=',startingframe
# print 'ending frames=',endingframe


cv2.destroyAllWindows()
