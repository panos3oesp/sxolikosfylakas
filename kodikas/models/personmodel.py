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
from dbmanager import *

class PersonModel:

    def getAll(self):
        db=DbManager("robot2.sqlite")
        persons=db.runSelect("SELECT * FROM Person")
        return persons



#a=PersonModel()
#persons = a.getAll()
#print(persons)