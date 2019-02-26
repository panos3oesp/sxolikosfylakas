#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathitis
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#from Helpers.dbmanager import *
from  Helpers.DbManager import *
class PersonModel:
    def __init__(self,dbPath):
        self.dbPath = dbPath
    def getAll(self):
        
        db=DbManager(self.dbPath)
        persons=db.runSelect("SELECT * FROM Person")
        return persons



#a=PersonModel()
#persons = a.getAll()
#print(persons)
