import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('prasadanxian@gmail.com','password here')
server.sendmail('prasadanxian@gmail.com','ginnarapuprasad@gmail.com','This is message by Python code')
print('mail Sent')

##before run this code> goto gmail >>and manage >>account >> security>>
##turn On (allow less secure apps)
