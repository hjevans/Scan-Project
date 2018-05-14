import RPi.GPIO as GPIO
import time

def entrySensor():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN)
    GPIO.setup(7,GPIO.IN)
    sense = GPIO.input(11) & GPIO.input(7)
    #while not sense:
        #sense = GPIO.input(11)
    time.sleep(.25)
    return sense

def exitSensor():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15,GPIO.IN)
    GPIO.setup(13,GPIO.IN)
    motion = GPIO.input(15) & GPIO.input(13)
    #while not motion:
        #motion = GPIO.input(15)
    time.sleep(.25)
    return motion

#def carExit():
 #   GPIO.setwarnings(False)
  #  GPIO.setmode(GPIO.BOARD)
   # GPIO.setup(15,GPIO.IN)
    #pres = GPIO.input(15)
    #while pres:
     #   pres = GPIO.input(15)
      #  time.sleep(.5)
   # return pres
        
    
