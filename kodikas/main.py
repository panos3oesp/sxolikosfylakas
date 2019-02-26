from  configuration import *
from  models.personmodel import *

confManager =  ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
print("Hello World")
personModel=PersonModel(confManager.dbPath)
persons = personModel.getAll()
print(persons)
