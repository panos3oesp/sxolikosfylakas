#Δοκιμαστικός κώδικας για να σταματάει τα μοτερ αν παραμείνουν κλειστά

from controllers.moveController import *
from Helpers.MediaHelper import *
mediaHelper = MediaHelper()
moveController = MoveController(mediaHelper)
moveController.stop() #κλεισε τα μοτερ
