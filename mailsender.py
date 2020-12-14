import settings_reader
import smtplib
import ssl
import datetime

# "gebräuchliche" Formatierungen und Berechnungen für die Darstellung der Zeit in er Mail:
# Formatvorlage für ein Datumsformat im "dd.mm.yyyy hh:mm"-Format mit einem trennenden "um" zwischen den Stunden und dem Datum.
DATE_FORMAT: str = "%d.%m.%Y um %H:%M"

# Formatiert die Gegebenen Sekunden und Mikrosekunden so, dass die Sekunden und 3 Nachkommastellen angezeigt werden.
def format_seconds(duration: datetime.timedelta) -> str:

    # Formatieren der Sekunden:
        # Tausendertrennzeichen '_'
        # Komma: '.'
        # Nachkommastellen: 3
    seconds = "{0:_.3f}".format(duration.total_seconds())

    # Ersetzen des Punktes durch ein Komma
    seconds = seconds.replace(".", ",")

    # Tausendertrennzeichen zu Punkten
    seconds = seconds.replace("_", ".")
    return seconds


def send_mail(subject: str, content: str) -> None:

    # Mailsendedaten (Server, Adressen, ...) laden
    maildata: dict = settings_reader.get_E_Mail_data()

    message: str = __build_message(subject, content)
    

    # Einstellen des Servers
    with smtplib.SMTP_SSL(maildata["sender_host"], maildata["server_port"], context=ssl.create_default_context()) as server:

        # Sender anmelden
        server.login(maildata["sender_adress"], maildata["sender_password"])

        # E-Mail schreiben und absenden
        server.sendmail(maildata["sender_adress"], maildata["receiver_adress"], message)


def __build_message(subject: str, content: str) -> str:

    # Nachricht Zusammenbauen, den Betreff mit zwei Leerzeilen vom Inhalt trennen
    message: str = "Subject: " + subject
    
    # Zeichensatz der Nachricht einstellen, damit Sonderzeichen auch funktionieren.
    message += "Content-Type: text/html; charset=utf-8\n\n"
    message = message.encode("UTF-8")

    # Inhalt der Nachricht anhängen
    message += content

    return message
