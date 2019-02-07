import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
email = "robo3epal@gmail.com"
server.login(email, "robotaki")
server.sendmail(email, email, "KALIMERA TI KANETE")
server.quit()
