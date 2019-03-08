


import RPi.GPIO as GPIO
import time
class MoveController:
    def __init__ (self):
        self.DISTANCE2STOP = 50
        self.DISTANCE2TURN = 30
        self.currentDirection="f"
        self.sensor1="1"
        self.sensor2="2"
        self.sensor3="3"
        self.sensor4="4"
        self.move=""
        self.PIN = 18
        self.PWMA1 = 6
        self.PWMA2 = 13
        self.PWMB1 = 20
        self.PWMB2 = 21

        self.PWMA1 = 6
        self.PWMA2 = 13
        self.PWMB1 = 20
        self.PWMB2 = 21

        self.D1 = 12
        self.D2 = 26
        self.PWM = 50
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PIN,GPIO.IN,GPIO.PUD_UP)

        GPIO.setup(self.PWMA1,GPIO.OUT)
        GPIO.setup(self.PWMA2,GPIO.OUT)
        GPIO.setup(self.PWMB1,GPIO.OUT)
        GPIO.setup(self.PWMB2,GPIO.OUT)
        GPIO.setup(self.D1,GPIO.OUT)
        GPIO.setup(self.D2,GPIO.OUT)
        self.p1 = GPIO.PWM(self.D1,500)
        self.p2 = GPIO.PWM(self.D2,500)

        

        self.p1.start(100)
        self.p2.start(100)
    def getDistance(self,sensor):
        return input("Dose apostasi aisthitira "+sensor)
    def move(self):
        frontDistance = self.getDistance(self.sensor1)
        backDistance = self.getDistance(self.sensor2)
        rightDistance = self.getDistance(self.sensor3)
        leftDistance = self.getDistance(self.sensor4)

        if frontDistance > self.DISTANCE2STOP:
            self.currentDirection = "f"
            self.forward()                    
        else:     
            if self.currentDirection == "f":
                self.stop()
                
            if rightDistance > self.DISTANCE2TURN:
                self.currentDirection = "r"
                self.right()
            else:
                if leftDistance > self.DISTANCE2TURN:
                    self.currentDirection = "l"
                    self.left()
                else:
                    self.currentDirection = "b"
                    reverse()





    def set_motor(self,A1,A2,B1,B2):
        GPIO.output(self.PWMA1,A1)
        GPIO.output(self.PWMA2,A2)
        GPIO.output(self.PWMB1,B1)
        GPIO.output(self.PWMB2,B2)

    def forward(self):
            GPIO.output(self.PWMA1,1)
            GPIO.output(self.PWMA2,0)
            GPIO.output(self.PWMB1,1)
            GPIO.output(self.PWMB2,0)

    def stop(self):
            self.set_motor(0,0,0,0)

    def reverse(self):
            self.set_motor(0,1,0,1)

    def left(self):
            self.set_motor(1,0,0,1)

    def right(self):
            self.set_motor(0,1,1,0)
'''
    def set_motor(A1,A2,B1,B2):
        GPIO.output(self.PWMA1,A1)
        GPIO.output(self.PWMA2,A2)
        GPIO.output(self.PWMB1,B1)
        GPIO.output(self.PWMB2,B2)

   def forward():
            GPIO.output(self.PWMA1,1)
            GPIO.output(self.PWMA2,0)
            GPIO.output(self.PWMB1,1)
            GPIO.output(self.PWMB2,0)

    def stop():
            set_motor(0,0,0,0)

    def reverse():
            set_motor(0,1,0,1)

    def left():
            set_motor(1,0,0,0)

    def right():
            set_motor(0,0,1,0)'''
