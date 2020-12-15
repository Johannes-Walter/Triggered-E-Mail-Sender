import databasemanager
import mailsender
import datetime

def send_daily_update() -> None:
    subject = "Daily update"
    message = ""

    # Liste mit den Knopfdrückungen der letzten 24h anfordern
    button_pressings: list = databasemanager.get_presses_since(datetime.datetime.now() - datetime.timedelta(days=1))

    # Je nach Anzahl der Betätigungen des Knopfes wird eine andere E-Mail geschrieben.
    if len(button_pressings) == 0:
        message = "In den letzten 24 Stunden wurde der Knopf leider kein einziges mal gedrückt."

    elif len(button_pressings) == 1:
        message = "Der Knopf wurde in den letzten 24 Stunden nur ein mal für {0} Sekunden gedrückt.".format(
            mailsender.format_seconds(button_pressings[2]))

    else:
        message += "Der Knopf wurde in den letzten 24 Stunden {0} mal gedrückt.\n".format(len(button_pressings))
        message += "Dabei wurde er in der Zeit für {0} Sekunden, also Durchschnittlich {1} Sekunden betätigt.".format(
            mailsender.format_seconds(calculate_pushtime(button_pressings)), 
            mailsender.format_seconds(calculate_averange_pushtime(button_pressings))
        )

    mailsender.send_mail(subject, message)


def calculate_averange_pushtime(button_pressings: list) -> datetime.timedelta:
    return calculate_pushtime(button_pressings) / len(button_pressings)


def calculate_pushtime(button_pressings: list) -> datetime.timedelta:
    pushtime: datetime.timedelta = datetime.timedelta()

    for press in button_pressings:
        # Position 2 ist die Druckdauer, die drückzeit wird aus allen in der Liste enthaltenen Zeiten zusammengerechnet.
        pushtime += press[2]

    return pushtime


if __name__ == "__main__":
    send_daily_update()