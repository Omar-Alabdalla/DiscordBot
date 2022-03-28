import smtplib
import ssl

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
