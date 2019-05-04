#-------------------------------------------------------------------------------
# Name:        sxolikos fylakas
# Purpose:     κεντρικό πρόγραμμα για το ρομποτ ΛΕΛΑ
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------

from configuration import *
from models.personmodel import *
from Helpers.MediaHelper import *
from controllers.moveController import *
from controllers.FaceRecognition import *
from datetime import datetime
import random


# πάρε τις ρυθμίσεις στο σχετικό class
confManager = ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
mediaHelper = MediaHelper() #instance του media manager για ήχο και εικόνα
faceRecognition = FaceRecognition(confManager,mediaHelper) # instance του face recognition controller

#όλες οι πιθανές καταστάσεις του ρομπότ σε λιστα
toDoChoices = ['relax', 'playmusic', 'facerecognition','move','giatre'] 

katastasi = "αρχική"
moveController = MoveController(mediaHelper)
moveController.stop() # σταμάτα τα μοτερ (αν ειχαν μεινει ανοικτά 
#faceRecognition.faceAnalysis()  #κάνε ανάλυση των προσώπων της βάσης δεδομένων
while True:  #για πάτα
    imeraEbdomadas = int(datetime.now().strftime('%w'))  # πάρε την ημέρα της εβδομάδας
    ora = int(datetime.now().strftime('%-H')) # πάρε την ώρα 
    lepta = int(datetime.now().strftime('%-M')) # πάρε το σε ποιο λεπτό είμαστε
    
    if imeraEbdomadas!=0 and imeraEbdomadas!=6 and ora>=10 and ora <= 23 and False: # αν ανοικτό το σχολείο
        if katastasi!="βοηθός": #αν άλλαξε η κατάσταση πες το
            katastasi="βοηθός"
            mediaHelper.playStringAsSound("Μπαίνω σε κατάσταση βοηθού")
            print("βοηθός")
        tiNaKano = random.choice(toDoChoices) #πάρε τυχαία κατάσταση
        #pesTi = input("Τι να κάνω; ")
        #tiNaKano = toDoChoices[int(pesTi)]
        if tiNaKano == 'relax':  #αν relax κοιμήσου για 10 δεύτερα
            print("relax")
            mediaHelper.playStringAsSound("ας κοιμηθώ λίγο")
            time.sleep(10)
        elif tiNaKano=='playmusic': #αν playmusic πες το και παίξει μουσική
            print("play music")
            mediaHelper.playStringAsSound("ας παίξω μουσική")
            mediaHelper.playRandomMusic()
        elif tiNaKano=='facerecognition':  #αν αναγνώριση προσώπου πες το και αναγνώρισε
            print("face rec")
            mediaHelper.playStringAsSound("θα αναγνωρίσω")
            
            faceRecognition.recognise()
        elif tiNaKano=='giatre': #αν giatre πες γεια σου γιατρέ μου :-)
            print("giatre")
            mediaHelper.playStringAsSound("γεια σου γιατρέ μου")  
        elif tiNaKano=='testDistances': #αυτό ειναι για έλεγχο μόνο αποστάσεων δεν κανει κάτι κανονικά
            mediaHelper.playStringAsSound("ας ελέγξω αποστάσεις")
            logFile = open("distanceLog.txt","w")
            moveController.testDistances(logFile)
            logFile.close()
        else: # αλλιως πες οτι θα ξεκινήσεις και βάλε τον movecontroller να δώσει ρεύμα στα μοτερ
            mediaHelper.playStringAsSound("ας κάνω μια βολτίτσα")
            print("move")
            logFile = open("distanceLog.txt","w")
            moveController.stop()
            for i in range(5000):
                moveController.move(logFile)
            moveController.stop()
            logFile.close()

                
            
            
    else:  #αν κλειστό σχολείο
        if katastasi!="φύλακας":
           katastasi="φύλακας"
           print("φύλακας")
           mediaHelper.playStringAsSound("Μπαίνω σε κατάσταση φύλακα") # πες την κατάσταση
           faceRecognition.recognise(True) # κάνε αναγνώριση αλλά αν ξένος σήμανε συναγερμό..

     





