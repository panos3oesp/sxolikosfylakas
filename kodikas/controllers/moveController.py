#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathitis
#
# Created:     27/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
class MoveController:
    def __init__ (self,sensor1,sendor2,sensor3,sensor4,move):
        self.DISTANCE2TURN = 30
        self.sensor1="1"
        self.sensor2="2"
        self.sensor3="3"
        self.sensor4="4"
        self.move=""
        self.PIN = 18
        self.self.PWMA1 = 6
        self.self.PWMA2 = 13
        self.self.PWMB1 = 20
        self.self.PWMB2 = 21
        self.D1 = 12
        self.D2 = 26
        self.PWM = 50
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PIN,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.self.PWMA1,GPIO.OUT)
        GPIO.setup(self.self.PWMA2,GPIO.OUT)
        GPIO.setup(self.self.PWMB1,GPIO.OUT)
        GPIO.setup(self.self.PWMB2,GPIO.OUT)
        GPIO.setup(self.D1,GPIO.OUT)
        GPIO.setup(self.D2,GPIO.OUT)
        self.p1 = GPIO.self.PWM(self.D1,500)
        self.p2 = GPIO.self.PWM(self.D2,500)
        self.p1.start(50)
        self.p2.start(50)
    def getDistance(self,sensor):
        return input("Dose apostasi aisthitira "+sensor)
    def move(self):
        frontDistance = self.getDistance(self.sensor1)
        backDistance = self.getDistance(self.sensor2)
        rightDistance = self.getDistance(self.sensor3)
        leftDistance = self.getDistance(self.sensor4)

        if frontDistance > self.DISTANCE2TURN:
            self.forward()
        else:
            if rightDistance > self.DISTANCE2TURN:
                self.right()
            else:
                if leftDistance > self.DISTANCE2TURN:
                    self.left()
                else:
                    reverse()




    def set_motor(A1,A2,B1,B2):
        GPIO.output(self.self.PWMA1,A1)
        GPIO.output(self.self.PWMA2,A2)
        GPIO.output(self.self.PWMB1,B1)
        GPIO.output(self.self.PWMB2,B2)

    def forward():
            GPIO.output(self.self.PWMA1,1)
            GPIO.output(self.self.PWMA2,0)
            GPIO.output(self.self.PWMB1,1)
            GPIO.output(self.self.PWMB2,0)

    def stop():
            set_motor(0,0,0,0)

    def reverse():
            set_motor(0,1,0,1)

    def left():
            set_motor(1,0,0,0)

    def right():
            set_motor(0,0,1,0)
    '''def getkey():
        if GPIO.input(self.PIN) == 0:
            count = 0
            while GPIO.input(self.PIN) == 0 and count < 200:  #9ms
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(self.PIN) == 1 and count < 80:  #4.5ms
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
                count = 0
                while GPIO.input(self.PIN) == 0 and count < 15:    #0.56ms
                    count += 1
                    time.sleep(0.00006)
                count = 0
                while GPIO.input(self.PIN) == 1 and count < 40:   #0: 0.56ms
                    count += 1                               #1: 1.69ms
                    time.sleep(0.00006)
                if count > 8:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
                return data[2]

        print('IRM Test Start ...')
        stop()
        try:
            while True:
                key = getkey()
                if(key != None):
                    print("Get the key: 0x%02x" %key)
                    if key == 0x18:
                        forward()
                        print("forward")
                    if key == 0x08:
                        left()
                        print("left")
                    if key == 0x1c:
                        stop()
                        print("stop")
                    if key == 0x5a:
                        right()
                        print("right")
                    if key == 0x52:
                        reverse()
                        print("reverse")
                    if key == 0x15:
                        if(self.PWM + 10 < 101):
                            self.PWM = self.PWM + 10
                            self.p1.ChangeDutyCycle(self.PWM)
                            self.p2.ChangeDutyCycle(self.PWM)
                            print(self.PWM)
                        if key == 0x07:
                            if(self.PWM - 10 > -1):
                                self.PWM = self.PWM - 10
                                self.p1.ChangeDutyCycle(self.PWM)
                                self.p2.ChangeDutyCycle(self.PWM)
                                print(self.PWM)
        except KeyboardInterrupt:
            GPIO.cleanup();
'''



