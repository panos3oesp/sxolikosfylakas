#-------------------------------------------------------------------------------
# Name:        person model
# Purpose:     κλάση που παίρνει από τη βάση δεδομένων όλα τα πρόσωπα, τα ονόματα και τα image paths 
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
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
