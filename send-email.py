import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "YOUR EMAIL"
toaddr = "RECEIVER EMAIL"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = "TEXT YOU WANT TO SEND"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "NAME OF YOUR FILE"
attachment = open("PATH OF YOUR FILENAME", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# SOME HELPFUL TUTORIALS

# https://null-byte.wonderhowto.com/how-to/send-anonymous-emails-with-python-0163091/
# http://naelshiab.com/tutorial-send-email-python/
# http://stackoverflow.com/questions/24270715/send-anonymous-mail-from-local-pc
# http://pastebin.com/p3i6h59A
# http://www.tutorialspoint.com/python/python_sending_email.htm --> to insert attachment
