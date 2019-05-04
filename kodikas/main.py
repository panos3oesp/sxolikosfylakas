from configuration import *
from models.personmodel import *
from Helpers.MediaHelper import *
from controllers.moveController import *
from controllers.FaceRecognition import *
from datetime import datetime
import random



confManager = ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
mediaHelper = MediaHelper()
faceRecognition = FaceRecognition(confManager,mediaHelper)

#faceRecognition.faceAnalysis()

'''print("Hello World")
personModel=PersonModel(confManager.dbPath)
persons = personModel.getAll()
print(persons)
mediaHelper.playStringAsSound("Καλημέρα")'''


toDoChoices = ['relax', 'playmusic', 'facerecognition','move','giatre']
toDoChoices = ['relax', 'playmusic', 'facerecognition','giatre']
#toDoChoices = ['relax', 'playmusic', 'facerecognition','giatre']
##toDoChoices = ['move']

katastasi = "αρχική"
moveController = MoveController(mediaHelper)
moveController.stop()
#faceRecognition.faceAnalysis()
while True:
    imeraEbdomadas = int(datetime.now().strftime('%w'))
    ora = int(datetime.now().strftime('%-H'))
    lepta = int(datetime.now().strftime('%-M'))
    print("here")
    if imeraEbdomadas!=0 and imeraEbdomadas!=6 and ora>=10 and ora <= 23 and False:
        if katastasi!="βοηθός":
            katastasi="βοηθός"
            mediaHelper.playStringAsSound("Μπαίνω σε κατάσταση βοηθού")
            print("βοηθός")
        tiNaKano = random.choice(toDoChoices)
        #pesTi = input("Τι να κάνω; ")
        #tiNaKano = toDoChoices[int(pesTi)]
        if tiNaKano == 'relax':
            print("relax")
            mediaHelper.playStringAsSound("ας κοιμηθώ λίγο")
            time.sleep(10)
        elif tiNaKano=='playmusic':
            print("play music")
            mediaHelper.playStringAsSound("ας παίξω μουσική")
            mediaHelper.playRandomMusic()
        elif tiNaKano=='facerecognition':
            print("face rec")
            mediaHelper.playStringAsSound("θα αναγνωρίσω")
            
            faceRecognition.recognise()
        elif tiNaKano=='giatre':
            print("giatre")
            mediaHelper.playStringAsSound("γεια σου γιατρέ μου")
        elif tiNaKano=='testDistances':
            mediaHelper.playStringAsSound("ας ελέγξω αποστάσεις")
            logFile = open("distanceLog.txt","w")
            moveController.testDistances(logFile)
            logFile.close()
        else:
            mediaHelper.playStringAsSound("ας κάνω μια βολτίτσα")
            print("move")
            logFile = open("distanceLog.txt","w")
            moveController.stop()
            for i in range(5000):
                moveController.move(logFile)
            moveController.stop()
            logFile.close()

                
            
            
    else:
        if katastasi!="φύλακας":
           katastasi="φύλακας"
           print("φύλακας")
           mediaHelper.playStringAsSound("Μπαίνω σε κατάσταση φύλακα")
           faceRecognition.recognise(True)

     




'''
moveController = MoveController(mediaHelper)
print("stopping controller")
moveController.stop()

for i in range(30000):
    moveController.move()
    
    
moveController.stop()
'''





'''mediaHelper.playStringAsSound("Παω μπροστά")
print("forward controller")
for i in range(300000):
        
        moveController.forward()
mediaHelper.playStringAsSound("Παω πίσω")
print("backward controller")
for i in range(300000):
        
        moveController.reverse()
mediaHelper.playStringAsSound("Παω αριστερά")
for i in range(300000):
        
        moveController.left()
mediaHelper.playStringAsSound("Παω δεξιά")
for i in range(300000):
        
        moveController.right()

moveController.stop()
'''
