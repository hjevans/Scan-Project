from sensors import entrySensor
from sensors import exitSensor
from cheese import cheese
from cheese import calibrate
import time
import datetime
import os
import cv2

frameRt = .5

today = datetime.datetime.now().strftime('%Y-%m-%d')
path = '/media/usb/' + today
if not os.path.isdir(path):
    os.makedirs(path)

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(3)
# initialize cameras
calibrate(cap0,cap1,cap2,cap3,1280,720,255,50,100,path)
time.sleep(1)

# calibrate cameras w 1920 h 1080 bright 100 contr idk satr idk bal idk
while True:
    while not entrySensor():
        print 'no car'
        
    entryTime = datetime.datetime.now().strftime('%Hhr-%Mmin-%Ssec')                                             
    car = path + '/' + entryTime
    os.makedirs(car)
    #print 'Car in!'
    itr = 0

    while not exitSensor():
        #print 'still in'
        cheese(cap0,cap1,cap2,cap3,car,itr)
        itr+=1
        time.sleep(frameRt)
    #print 'Begin car exit'

    while exitSensor():
        print 'exiting'
        cheese(cap0,cap1,cap2,cap3,car,itr)
        itr+=1
        time.sleep(frameRt)
    #print 'mission complete'
    time.sleep(2)

