import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mailFunctions
import Token

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = Token.EmailAddress()  # Enter your email address
password = Token.Password()  # Enter your Email Password


def sendMail(rmail, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, rmail, message)


def sendHTMLmail(rmail, html):
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = rmail

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, rmail, message.as_string()
        )


def sendFileMail(rmail, a, senderDiscord):
    mail_content = f'''Hello,
    Discord user: {senderDiscord} wanted to send you this file for whatever reason.
    '''
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = rmail
    message['Subject'] = 'A email sent utilizing python(File Included).'

    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = a
    print(attach_file_name)
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(attach_file.read())
    encoders.encode_base64(payload)  # encode the attachment

    # add payload header with filename
    payload.add_header('Content-Decomposition',
                       'attachment', filename=attach_file_name)
    message.attach(payload)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_email, password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_email, rmail, text)
    session.quit()
    print('Mail Sent')
