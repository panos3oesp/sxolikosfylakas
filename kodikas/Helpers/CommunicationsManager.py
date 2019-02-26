import smtplib
class CommunicationsManager:
  def __init__(self,email,adminMail,mailPassword):
    self.email = email
    self.adminMail = adminMail,
    self.mailPassword = mailPassword
  def sendMail(self,message): 
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(self.email, self.mailPassword)
    server.sendmail(self.email, self.adminMail, message)
    server.quit()
    
