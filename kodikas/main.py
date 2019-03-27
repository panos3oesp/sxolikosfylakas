from  configuration import *
from  models.personmodel import *
from Helpers.MediaHelper import *
from controllers.moveController import *
from datetime import datetime
import random



confManager =  ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
'''print("Hello World")
personModel=PersonModel(confManager.dbPath)
persons = personModel.getAll()
print(persons)
mediaHelper.playStringAsSound("Καλημέρα")'''


toDoChoices = ['relax', 'playmusic', 'facerecognition','move']
mediaHelper = MediaHelper()
katastasi = "αρχική"


while True:
    imeraEbdomadas = int(datetime.now().strftime('%w'))
    ora = int(datetime.now().strftime('%-H'))
    lepta = int(datetime.now().strftime('%-M'))

    if imeraEbdomadas!=0 and imeraEbdomadas!=6 and ora>=18 and ora <= 22:
        if katastasi!="βοηθός":
            katastasi="βοηθός"
            mediaHelper.playStringAsSound("Μπαίνω σε κατάσταση βοηθού")
        tiNaKano = random.choice(toDoChoices)
        if tiNaKano == 'relax':
            mediaHelper.playStringAsSound("ας κοιμηθω λίο")
            time.sleep(180)
        elif tiNaKano=='playmusic':
            mediaHelper.playStringAsSound("θα παίξω τραλαλά")
        elif tiNaKano=='facerecognition':
            mediaHelper.playStringAsSound("θα ανανωρίσω")

        else:
            mediaHelper.playStringAsSound("ας κάνω μια βολτίτσα")
                
            
            
    else:
        if katastasi!="φύλακας":
           katastasi="φύλακας"
           mediaHelper.playStringAsSound("Μπαίνω σε κατάσταση φύλακα")                
        

     




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
