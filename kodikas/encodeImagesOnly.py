from configuration import *
from models.personmodel import *
from Helpers.MediaHelper import *
from controllers.moveController import *
from controllers.FaceRecognition import *
from datetime import datetime
import random


confManager = ConfigurationManager("11:00","8:00","res/robot2.sqlite","res/images/faces/")
mediaHelper = MediaHelper()
faceRecognition = FaceRecognition(confManager)
print("Start")
faceRecognition.justEncode()
