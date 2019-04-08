import RPi.GPIO as GPIO
import time
import serial


class MoveController:
    def __init__ (self,mediaHelper):
        self.DISTANCE2STOP = 100
        self.DISTANCE2TURN = 100
        self.currentDirection="f"
        self.sensor1=0
        self.sensor2=1
        self.sensor3=2
        self.sensor4=3
        self.mediaHelper = mediaHelper
        
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
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
        

        self.p1.start(60)
        self.p2.start(65)

        self.fm = 0
    def getDistance(self,sensor):
        try:
            #time.sleep(1)
            distance = self.ser.readline()
            distance = distance.decode("utf-8")
            if distance.strip()=="":
                return [-1,-1,-1,-1]
            
            #print(distance)        
            #time.sleep(0.125)
            print("#########")
            
            distanceArray = distance.split(',')
            if "" in distanceArray:
                return [-1,-1,-1,-1]
            print(distanceArray)
            print ("sensor", sensor)
            return distanceArray
            if distanceArray[sensor] != "":
                return distanceArray[sensor]
            else:
                return [-1,-1,-1,-1]
        except:
            return [-1,-1,-1,-1]
        
    def move(self):
        distanceArray = self.getDistance(self.sensor1)
        if(len(distanceArray)==4):
            frontDistance = float(distanceArray[2])
            backDistance = float(distanceArray[0])
            rightDistance = float(distanceArray[3])
            leftDistance = float(distanceArray[1])
        else:
            frontDistance = -1
            backDistance =  -1 
            rightDistance =  -1
            leftDistance =  -1

        self.ser.flushInput()
        self.ser.flushOutput()
        print("Front Distance:",frontDistance)
        print("Right Distance:",rightDistance)
        print("Left Distance:",leftDistance)
        print("Back Distance:",backDistance)

        if (frontDistance < self.DISTANCE2STOP) or (self.currentDirection == "f" and frontDistance==-1) :
            #if self.currentDirection != "f":
             #   self.p1.start(60)
              #  self.p2.start(65)
            self.fm+=1
            if self.fm == 800:
                self.stop()
                time.sleep(1)
                self.fm=0
            else:
                self.currentDirection = "f"
                self.forward()
                
        else:     
            #if self.currentDirection == "f":
                #self.stop()
                
            if (rightDistance < self.DISTANCE2TURN) or (self.currentDirection == "r" and frontDistance==-1):
                if self.currentDirection != "r":
                    self.stop()
                    time.sleep(1)
                    
                else:
                    self.right()
                self.currentDirection = "r"
            else:
                if (leftDistance < self.DISTANCE2TURN) or (self.currentDirection == "l" and frontDistance==-1):
                    if self.currentDirection != "l":
                        self.stop()
                        time.sleep(1)
                    
                    else:
                        self.left()
                else:
                    self.currentDirection = "b"
                    self.reverse()





    def set_motor(self,A1,A2,B1,B2):
        GPIO.output(self.PWMA1,A1)
        GPIO.output(self.PWMA2,A2)
        GPIO.output(self.PWMB1,B1)
        GPIO.output(self.PWMB2,B2)

    def forward(self):
        self.mediaHelper.playStringAsSound("Παω μπροστά")
        GPIO.output(self.PWMA1,1)
        GPIO.output(self.PWMA2,0)
        GPIO.output(self.PWMB1,1)
        GPIO.output(self.PWMB2,0)
        print("f")
    def stop(self):
        self.mediaHelper.playStringAsSound("Σταματάω")
        self.set_motor(0,0,0,0)
    def reverse(self):
        self.mediaHelper.playStringAsSound("Κάνω πίσω")
        self.set_motor(0,1,0,1)
        print("r")

    def left(self):
        self.mediaHelper.playStringAsSound("Παω δεξιά")
        self.set_motor(1,0,0,1)
        print("l")

    def right(self):
        self.mediaHelper.playStringAsSound("Παω αριστερά")
        self.set_motor(0,1,1,0)
        print("r")

