import cv2
import time
import os

def calibrate(cap0,cap1,cap2,cap3,width,height,bright,contr,satr,path):
    cap0.set(3,width) #width
    cap0.set(4,height) #height
    cap1.set(3,width) #width
    cap1.set(4,height)
    cap2.set(3,width) #width
    cap2.set(4,height)
    cap3.set(3,width) #width
    cap3.set(4,height)
    
    time.sleep(4)
    
    cap0.set(10,bright) #brightness
    cap0.set(11,contr) #contrast
    cap0.set(12,satr) # saturation (0,255,1)
    
    time.sleep(2)
    
    cap1.set(10,bright)
    cap1.set(11,contr)
    cap1.set(12,satr)
    
    time.sleep(2)
    
    cap2.set(10,bright)
    cap2.set(11,contr)
    cap2.set(12,satr)
    
    time.sleep(2)
    
    cap3.set(10,bright)
    cap3.set(11,contr)
    cap3.set(12,satr)
    
    time.sleep(4)
    
    ret0,frame0 = cap0.read()
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    ret3,frame3 = cap3.read()
    
    #for i in range(10):
     #   j = str(i)
    os.chdir(path)
    cv2.imwrite('CALIBRATION0.jpg',frame0)
    cv2.imwrite('CALIBRATION1.jpg',frame1)
    cv2.imwrite('CALIBRATION2.jpg',frame2)
    cv2.imwrite('CALIBRATION3.jpg',frame3)


def cheese(cap0,cap1,cap2,cap3,path,itr):
#    t = time.time()
#   st = datetime.datetime.fromtimestamp(t).strftime('%Hhr%Mmin%Ssec')
    ret0,frame0 = cap0.read()
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    ret3,frame3 = cap3.read()
    itr = str(itr)
    os.chdir(path)
    cv2.imwrite(itr+'-cam0.jpg',frame0)
    cv2.imwrite(itr+'-cam1.jpg',frame1)
    cv2.imwrite(itr+'-cam2.jpg',frame2)
    cv2.imwrite(itr+'-cam3.jpg',frame3)

    os.chdir('/home/pi')

    
