# Κώδικας που τρέχει αυτόνομα και δημιουργεί το αρχείο με τις αναλύσεις των προσώπων που περιέχονται στις φωτογραφίες.

from configuration import *
from models.personmodel import *
from Helpers.MediaHelper import *
from controllers.moveController import *
from controllers.FaceRecognition import *
from datetime import datetime
import random

# θέσε τις ρυθμίσεις
confManager = ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
mediaHelper = MediaHelper() #Κατασκεύασε instance το media manager για ηχο και media γενικότερα
faceRecognition = FaceRecognition(confManager) #Κατασκεύασε instance το face recognition controller για ανάλυση εικόνων
print("Start")
faceRecognition.justEncode() #κάνε την ανάλυση των εικόνων
