#-------------------------------------------------------------------------------
# Name:        onlyStop
# Purpose:     Δοκιμαστικός κώδικας για να σταματάει τα μοτερ αν παραμείνουν κλειστά
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------

from controllers.moveController import *
from Helpers.MediaHelper import *
mediaHelper = MediaHelper()
moveController = MoveController(mediaHelper)
moveController.stop() #κλεισε τα μοτερ
