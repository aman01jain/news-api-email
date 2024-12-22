import smtplib
import ssl


def email_send(message):
    host = "smtp.gmail.com"
    port = 465
    password = "prwv gqpp xckk jsob"
    username = "aman2022jain@gmail.com"
    reciever = "aman2022jain@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)


