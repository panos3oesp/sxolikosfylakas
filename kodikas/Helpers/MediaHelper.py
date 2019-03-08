from gtts import gTTS
import os

class MediaHelper:
   def __init__(self,imagePath,mp3Path):
        self.imagePath=imagePath
        self.mp3Path=mp3Path


   def playStringAsSound(self,theString):
      tts = gTTS(text=theString, lang='el')
      tts.save("temp.mp3")
      os.system("mpg321 temp.mp3")



#a=MediaHelper("res/mp3/")


#a.playMpe("LifeIsLife.mp3")

