#-------------------------------------------------------------------------------
# Name:        MainController
# Purpose:     παλιος controller, θα σβηστεί
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------

import random
class MainController:
    toDoChoices = ['relax', 'playmusic', 'facerecognition']
    def __init__(self):


    def getWhatToDo(self):
        return random.choice(toDoChoices)

