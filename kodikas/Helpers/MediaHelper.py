import playsound

class MediaHelper:
   def __init__(self,imagePath,mp3Path):
        self.imagePath=imagePath
        self.mp3Path=mp3Path

    def  playMp3(self,mp3File):
        playsound.playsound(mp3Path+mp3File, True)



#a=MediaHelper("res/mp3/")


#a.playMpe("LifeIsLife.mp3")

