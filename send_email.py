'''While run the file make sure (Allow less secure apps: ON)
'''

import smtplib


subject = input("Subject?<user inputs subject>")
body = input("Body? > <user inputs a one line email body>")
message = "Subject:{}\n\n{}".format(subject,body)
sender_email = "shreya@zelthy.com"
Recipient = input("Recipient? <user inputs the email address of the recipient>")
password = str("Enter your password")            # In place of Enter your password kindly put your password.
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Successful")
server.sendmail(sender_email, Recipient, message)
print("Email Sent!", Recipient)
server.quit()