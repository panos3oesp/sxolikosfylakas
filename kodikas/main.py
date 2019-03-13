from  configuration import *
from  models.personmodel import *
from Helpers.MediaHelper import *
from controllers.moveController import *

confManager =  ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
'''print("Hello World")
personModel=PersonModel(confManager.dbPath)
persons = personModel.getAll()
print(persons)



mediaHelper.playStringAsSound("Καλημέρα")'''
mediaHelper = MediaHelper()
moveController = MoveController()
print("stopping controller")
moveController.stop()
#for i in range(300000):
#        moveController.move()
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
