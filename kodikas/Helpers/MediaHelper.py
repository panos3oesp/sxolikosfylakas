#-------------------------------------------------------------------------------
# Name:        MediaHelper
# Purpose:     κλάση για να παίζει ήχους - text 2 speech -  speech to text
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------



from gtts import gTTS
import os
import speech_recognition as sr
import sys
import glob
import random

class MediaHelper:
   '''def __init__(self,imagePath,mp3Path):
        self.imagePath=imagePath
        self.mp3Path=mp3Path
'''
   def __init__(self):
      self.imagePath=""
   # παίξει string σαν ηχο μεσω google text2speech
   def playStringAsSound(self,theString):
      tts = gTTS(text=theString, lang='el') #κανε μετατροπή el για ελληνικά
      tts.save("temp.mp3") #φτιάξε προσωρινό αρχείο
      os.system("mpg321 temp.mp3") #παίξε προσωρινό αρχείο
   def speech2Text(self,question=""):  #ομιλία σε text
      if question!="":
         self.playStringAsSound(question)
      r = sr.Recognizer()
      with sr.Microphone() as source:
         audio = r.listen(source)

      try:
          youSaid=r.recognize_google(audio,language = 'el-GR')           
          return youSaid
      except sr.UnknownValueError:
         self.playStringAsSound("Δεν σε καταλαβαίνω")
         return ""
      except sr.RequestError as e:
         self.playStringAsSound("Δεν σε καταλαβαίνω")
         return ""
   # επιστρέφει ένα τυχαίο αρχείο από έναν φάκελο 
   # για να λαμβάνει το ρομπότ και να παίζει τυχαίο mp3
   def getRandomFile(self,pathFolder):
      files=glob.glob(pathFolder)
      return random.choice(files)
   #παίζει τυχαίο κομμάτι mp3 από φάκελο
   def playRandomMusic(self):
      randomFile = self.getRandomFile("res/music/*.mp3")
      os.system("mpg321 "+randomFile+" & sleep 10; killall mpg321")
      





