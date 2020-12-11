import settings_reader
import smtplib
import ssl
import datetime

def send_mail(subject: str, content: str):

    maildata = settings_reader.get_E_Mail_data()
    message = """Subject: {0}

{1}""".format(subject, content)
    print(message)
    
    # Einstellen des Servers
    with smtplib.SMTP_SSL(maildata["sender_host"], maildata["server_port"], context=ssl.create_default_context()) as server:

        # Sender anmelden
        server.login(maildata["sender_adress"], maildata["sender_password"])

        # E-Mail schreiben und absenden
        server.sendmail(maildata["sender_adress"], maildata["receiver_adress"], message)

    print("gesendet")


def send_button_press(press_start: datetime.datetime, press_duration: datetime.timedelta):

    # Das Datum im Tag.Monat.Jahr-Format und die Uhrzeit im Stunden:Minuten-Format formatieren
    date = press_start.strftime("dem %d.%m.%Y um %H:%M")

    # Die Dauer im Sekunden.Milisekunden-Format formatieren.
    # Da es im timedelta keine Milisekunden gibt, muss die sog. "floor division" verwendet werden.
    duration = "{0},{1}".format(press_duration.seconds, press_duration.microseconds // 1000)

    subject = "Der Knopf wurde gedrueckt!"
    message = """Am {0} wurde der Knopf fuer {1} Sekunden gedrueckt!""".format(date, duration)

    send_mail(subject, message)
