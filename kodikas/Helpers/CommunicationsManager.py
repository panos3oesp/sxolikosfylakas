#-------------------------------------------------------------------------------
# Name:        CommunicationsManager
# Purpose:     Κλάση για αποστολή email 
#
# Author:      μαθητες 3ι εσπερινό ΕΠΑΛ Ν. Φιλαδέφειας
#
# Created:     22/02/2019
# Copyright:   (c) mathitis 2019
# Licence:     ΜΙΤ
#-------------------------------------------------------------------------------

import smtplib
class CommunicationsManager:
  def __init__(self,email,adminMail,mailPassword):
    self.email = email #το εμαιλ αποστολής
    self.adminMail = adminMail # το email που θα παραλάβει
    self.mailPassword = mailPassword #το password
  def sendMail(self,message): 
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #σύνδεση με τον server
    server.login(self.email, self.mailPassword)  #κανε login
    server.sendmail(self.email, self.adminMail, message) #στείλε μήνυμα
    server.quit() #κλείσε σύνδεση
    
