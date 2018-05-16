from sensors import entrySensor
from sensors import exitSensor
from cheese import cheese
from cheese import calibrate
import time
import datetime
import os
import cv2

frameRt = .25

today = datetime.datetime.now().strftime('%Y-%m-%d')
path = '/media/usb/' + today
if not os.path.isdir(path):
    os.makedirs(path)

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(3)
# initialize cameras
calibrate(cap0,cap1,cap2,cap3,1280,720,100,100,125,path)
time.sleep(1)

# calibrate cameras w 1920 h 1080 bright 100 contr idk satr idk bal idk
while True:
    print 'initial entry = ' +str(entrySensor())
    while entrySensor():
        print 'entry ' + str(entrySensor())
    print 'initial exit = ' + str(exitSensor())
    while exitSensor():
        print 'exit '+ str(entrySensor())
    #entry = 0
    #while entrySensor():
        #entry = 0
    #exit = 0
    #while exitSensor():
    #    exit = 0
    #time.sleep(40)
    entry = 0
    while not entry:
        print 'no car'
        entry = entrySensor()
        
    entryTime = datetime.datetime.now().strftime('%Hhr-%Mmin-%Ssec')                                             
    car = path + '/' + entryTime
    os.makedirs(car)
    print 'Car in!'
    itr = -4
    
    exit = 0
    while not exit:
        print 'still in'
        cheese(cap0,cap1,cap2,cap3,car,itr)
        itr+=1
        time.sleep(frameRt)
        exit = exitSensor()
    print 'Begin car exit'

    while exitSensor():
        print 'exiting'
        cheese(cap0,cap1,cap2,cap3,car,itr)
        itr+=1
        time.sleep(frameRt)
        #exit = exitSensor()
    print 'mission complete'
    time.sleep(2)

