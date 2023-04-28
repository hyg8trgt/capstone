import cv2
import numpy as np
import time

video=cv2.VideoCapture(0,cv2.CAP_DSHOW)

time.sleep(3)
count=0
background=0
for i in range(60):
    check,background=video.read()
background=np.flip(background,axis=1)
while (video.isOpened()):
    dummy,image=video.read()
    if dummy ==  False:
        break
    count+=1
    image=np.flip(image,axis=1)
    hsc=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upper_red=np.array({int(10),int(255),int(255)})
    print(upper_red)
    mask1=cv2.inRange(hsc,lower_red,upper_red)
    lower_red=np.array([120,120,50])
    upper_red=np.array([int(180),int(255),int(255)])
    mask2=cv2.inRange(hsc,lower_red,upper_red)
    mask1+=mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    part1=cv2.bitwise_and(image,image,mask2)
    part2=cv2.bitwise_and(background,background=mask1)
    finaloutput=cv2.addWeighted(part1,1,part2,1,0)

    cv2.imshow("invisibility cloak", finaloutput)
    key=cv2.waitKey(25)
    
    if key == ord("c"):
        break
    video.release()
    cv2.destroyAllWindows()