import settings_reader
import smtplib
import ssl


def send_mail(subject: str, content: str):

    maildata = settings_reader.get_E_Mail_data()
    message = """Subject: {0}
    
    {1}""".format(subject, content)
    print(message)
    
    with smtplib.SMTP_SSL(maildata["sender_host"], maildata["server_port"], context=ssl.create_default_context()) as server:
        server.login(maildata["sender_adress"], maildata["sender_password"])
        server.sendmail(maildata["sender_adress"], maildata["receiver_adress"], message)