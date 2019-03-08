from  configuration import *
from  models.personmodel import *
from controllers.moveController import *

confManager =  ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
print("Hello World")
personModel=PersonModel(confManager.dbPath)
persons = personModel.getAll()
print(persons)

moveController = MoveController()
for i in range(1000000):
	moveController.forward()
for i in range(1000000):
	moveController.reverse()
for i in range(1000000):
	moveController.left()
for i in range(1000000):
	moveController.right()