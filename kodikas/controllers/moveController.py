#-------------------------------------------------------------------------------
# Name:        MoveController
# Purpose:     κλάση που ελέγχει την κίνηση του ρομπότ
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------

#κλάση που ελέγχει την κίνηση του ρομπότ
import RPi.GPIO as GPIO
import time
import serial


class MoveController:
    def __init__ (self,mediaHelper):
        self.DISTANCE2STOP = 180        #σε ποια απόσταση θα σταματάει
        self.DISTANCE2TURN = 180        #σε ποια απόσταση θα σβήνει
        self.currentDirection="f"       #κρατάει πως κινούταν έως τώρα
        #οι σένσορες βάση της λίστας που στέλνει το arduino
        self.sensor1=0
        self.sensor2=1
        self.sensor3=2
        self.sensor4=3
        
        #o media helper για να παίζει ήχο
        self.mediaHelper = mediaHelper
        
        
        #τα pins για το hat για να στέλνει δεδομένα
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
        
        #σετάρει τον controller κίνησης σύμφωνα με το documentation
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
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=None)
        
        #θέσε ποσοστό ταχύτητας στα μοτέρ
        self.p1.start(60)
        self.p2.start(60)

        self.fm = 0
        
    #μέθοδος για να ελέγχει τις αποστάσεις
    #μόνο για δοκιμαστικούς λόγους
    def testDistances(self,logFile):
        for i in range(500):
            #πάρε τις αποστάσεις
            distanceArray = self.getDistance()
            print(distanceArray)
            #αν έχει φέρει το arduino 4 αλλιως σκουπίδια
            if(len(distanceArray)==4):
                rightDistance = float(distanceArray[3])
                backDistance = float(distanceArray[0])
                frontDistance = float(distanceArray[2])
                leftDistance = float(distanceArray[1])
                #self.ser.flushInput()
                #self.ser.flushOutput()
            
                logFile.write(str(frontDistance)+"-"+str(backDistance)+"-"+str(rightDistance)+"-"+str(leftDistance)+"\r\n")
            #time.sleep(0.5)
        
        
    
    #πάρε τις αποστάσεις από το usb από το arduino    
    def getDistance(self):
        try:
            #time.sleep(1)
            distance = self.ser.readline()  #διάβασε usb
            distance = distance.decode("utf-8") #κάνε utf8
            if distance.strip()=="":    #αν κενό θελς -1 -1 -1 -1 άρα αγνόησε
                return [-1,-1,-1,-1]
            
            #print(distance)        
            #time.sleep(0.125)
            #print("#########")
            
            distanceArray = distance.split(',') #χώρισε με κομμα τις αποστάσεις σε λιστα
            if "" in distanceArray: #αν έχει κενα τότε σκουπίδια
                return [-1,-1,-1,-1]
            #print(distanceArray)
            #print ("sensor", sensor)
            return distanceArray    #αλλιώς επέστρεψε τις αποστάσεις σε λίστα πλέον
        #αν πάει κάτι στραβά τοτε επεστρεψε -1 -1 -1 -1    
        except:
            return [-1,-1,-1,-1]
        
    #μέθοδος για την κίνηση     
    #παράμετρος αν θες να τυπώνεται σε log οι αποστάσεις
    def move(self,logFile):
        
        self.fm = 0
        distanceArray = self.getDistance()  #πάρε απόσταση
        
        #αν φέρει 4 αποστάσεις φτιαξε τις μεταβλητές
        if(len(distanceArray)==4):
            rightDistance = float(distanceArray[3])
            backDistance = float(distanceArray[0])
            frontDistance = float(distanceArray[2])
            leftDistance = float(distanceArray[1])
        else:   #αλλιώς σκουπίδια
            frontDistance = -1
            backDistance =  -1 
            rightDistance =  -1
            leftDistance =  -1

        
        print(str(frontDistance - self.DISTANCE2STOP))
        #αν δεν έχει κάτι μπροστά ή πήραμε σκουπιδια και πήγαινε ήδη μπροστά
        if (frontDistance < self.DISTANCE2STOP) or (self.currentDirection == "f" and frontDistance==-1) :
            #if self.currentDirection != "f":
             #   self.p1.start(60)
              #  self.p2.start(65)
            self.fm+=1
            # για κάθε 100 στροφες σταμάτα λίγο γιατι τρέχεις
            if self.fm == 100:
                self.stop()
                time.sleep(1)
                self.fm=0
            else: #αλλιως πήγαινε απλά μπροστά
                self.currentDirection = "f"
                self.forward()
                
        else:     
            #if self.currentDirection == "f":
                #self.stop()
            #αν έχει κάτι μπροστά και όχι δεξιά ή πήγαινε ήδη δεξιά ΄και πήραμε σκουπιδια     
            if (rightDistance < self.DISTANCE2TURN) or (self.currentDirection == "r" and frontDistance==-1):
                self.right()
                #if self.currentDirection != "r":
                 #   self.stop()
                    #time.sleep(1)
                    
                #else:
                 #   self.right()
                self.currentDirection = "r"
            else:
                #αν έχει κάτι μπροστά και δεξιά και όχι αριστερά ή πήγαινε ήδη αριστερά ΄και πήραμε σκουπιδια 
                if (leftDistance < self.DISTANCE2TURN) or (self.currentDirection == "l" and frontDistance==-1):
                    self.left()
                    #if self.currentDirection != "l":
                        #self.stop()
                        #time.sleep(1)
                    
                    #else:
                     #   self.left()
                #αλλιώς πήγαινε πίσω
                else:
                    self.currentDirection = "b"
                    self.reverse()




    #θέσε ποιο ειναι το μοτέρ
    def set_motor(self,A1,A2,B1,B2):
        GPIO.output(self.PWMA1,A1)
        GPIO.output(self.PWMA2,A2)
        GPIO.output(self.PWMB1,B1)
        GPIO.output(self.PWMB2,B2)
    #πήγαινε μπροτά
    def forward(self):
        
        #self.mediaHelper.playStringAsSound("Παω μπροστά")
        GPIO.output(self.PWMA1,1)
        GPIO.output(self.PWMA2,0)
        GPIO.output(self.PWMB1,1)
        GPIO.output(self.PWMB2,0)
        #print("f")
    #σταμάτα
    def stop(self):
        #self.mediaHelper.playStringAsSound("Σταματάω")
        self.set_motor(0,0,0,0)
    #κάνε όπισθεν
    def reverse(self):
        #self.mediaHelper.playStringAsSound("Κάνω πίσω")
        self.set_motor(0,1,0,1)
        #print("r")
    #πήγαινε αριστερά
    def left(self):
        #self.mediaHelper.playStringAsSound("Παω δεξιά")
        self.set_motor(1,0,0,1)
        #print("l")
    #πήγαινε δεξιά
    def right(self):
        #self.mediaHelper.playStringAsSound("Παω αριστερά")
        self.set_motor(0,1,1,0)
        #print("r")

