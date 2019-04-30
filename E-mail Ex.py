import smtplib

smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
sender = 'example@example.com'
receivers = 'example2@example.com'
password = input(print('Please input your password'))

message = """From: Sender
To: Receiver
Subject: Hello!

Hello World!
"""

smtpObj.login(sender, password)

smtpObj.sendmail(sender, receivers, message)

smtpObj.quit()
