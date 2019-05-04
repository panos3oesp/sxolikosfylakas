# Κλαση πουτ συγκρατεί τις ρυθμίσεις της εφαρμογής.

class ConfigurationManager:
  def __init__(self,startGuardingTime,endGuardingTime,dbPath,faceImagesPath):
    self.startGuardingTime = startGuardingTime
    self.endGuardingTime = endGuardingTime
    self.dbPath = dbPath
    self.faceImagesPath = faceImagesPath
