import random
class MainController:
    toDoChoices = ['relax', 'playmusic', 'facerecognition']
    def __init__(self):


    def getWhatToDo(self):
        return random.choice(toDoChoices)

