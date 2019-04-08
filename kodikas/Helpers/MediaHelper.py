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
   def playStringAsSound(self,theString):
      tts = gTTS(text=theString, lang='el')
      tts.save("temp.mp3")
      os.system("mpg321 temp.mp3")
   def speech2Text(self,question=""):
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
   
   def getRandomFile(self,pathFolder):
      files=glob.glob(pathFolder)
      return random.choice(files)
   def playRandomMusic(self):
      randomFile = self.getRandomFile("res/music/*.mp3")
      os.system("mpg321 "+randomFile+" & sleep 10; killall mpg321")
      





