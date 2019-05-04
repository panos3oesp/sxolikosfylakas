#-------------------------------------------------------------------------------
# Name:        MediaHelper
# Purpose:     #κλαση υπεύθυνη για την κίνηση του ρομπότ
# δε χρειάζεται πια, θα σβηστεί
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------


import RPi.GPIO as GPIO #Import GPIO library
import time #Import time library 


class MotionHelper:
    def __init__(self):
        self.FRONTSENSOR=26
        self.BACKSENSOR=27
        self.LEFTSENSOR=28
        self.RIGHTSENSOR=29
        #GPIO.setmode(GPIO.BCM) 

    #dummy function θα σβηστεί
    def somethingMoved(self):
        if self.somethingMovedInSensor(self.FRONTSENSOR):
            return "FrontMovement"
        '''if self.somethingMovedInSensor(self.BACKSENSOR):
            return "BackMovement"
        if self.somethingMovedInSensor(self.LEFTSENSOR):
            return "LeftMovement"
        if self.somethingMovedInSensor(self.RIGHTSENSOR):
            return "RightMovement"'''


    
    def somethingMovedInSensor(self,pir):
        GPIO.setmode(GPIO.BOARD) #Set GPIO pin numbering 

        #pir = 26 #Associate pin 26 to pir 

        GPIO.setup(pir, GPIO.IN) #Set pin as GPIO in print "Waiting for sensor to settle" 
        
        time.sleep(2) #Waiting 2 seconds for the sensor to initiate print "Detecting motion" 



        if GPIO.input(pir): #Check whether pir is HIGH print "Motion Detected!" 
            time.sleep(2) #D1- Delay to avoid multiple detection
            time.sleep(0.1) #While loop delay should be less than detection(hardware) delay
            return True
        else:
            return False



motionHelper = MotionHelper()

while True:
    if motionHelper.somethingMoved()=="FrontMovement":
        print("Kati kounietai mprosta")
    elif motionHelper.somethingMoved()=="BackMovement":
        print("Kati kounietai piso")
    elif motionHelper.somethingMoved()=="LeftMovement":
        print("Kati kounietai aristera")
    elif motionHelper.somethingMoved()=="RightMovement":
        print("Kati kounietai dexia")
    else:
        print("###########")
    
