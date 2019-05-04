#-------------------------------------------------------------------------------
# Name:        ConfigurationManager
# Purpose:     Κλαση πουτ συγκρατεί τις ρυθμίσεις της εφαρμογής. 
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------


class ConfigurationManager:
  def __init__(self,startGuardingTime,endGuardingTime,dbPath,faceImagesPath):
    self.startGuardingTime = startGuardingTime
    self.endGuardingTime = endGuardingTime
    self.dbPath = dbPath
    self.faceImagesPath = faceImagesPath
