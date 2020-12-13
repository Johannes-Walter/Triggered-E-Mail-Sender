from io import DEFAULT_BUFFER_SIZE
from databasemanager import get_presses_since
from sqlite3.dbapi2 import SQLITE_REINDEX
import mailsender
import sqlite3
import datetime

def send_daily_update() -> None:
    subject = "Daily update"
    message = ""

    button_pressings: list = get_presses_since(datetime.datetime.now() - datetime.timedelta(days=1))

    if len(button_pressings) == 0:
        message = "In den letzten 24 Stunden wurde der Knopf leider kein einziges mal gedrückt."
    elif len(button_pressings) == 1:
        message = "Der Knopf wurde in den letzten 24 Stunden nur ein mal für {0} Sekunden gedrückt.".format(button_pressings[2])
    else:
        message += "Der Knopf wurde in den letzten 24 Stunden {0} mal gedrückt.\n".format(len(button_pressings))
        message += "Insgesamt wurde der Knopf in der Zeit für {0} Sekunden, also Durchschnittlich {1} Sekunden gedrückt.".format(
            calculate_pushtime(button_pressings), calculate_averange_pushtime(button_pressings)
        )

    print(message)
    mailsender.send_mail(subject, message)

def calculate_averange_pushtime(button_pressings: list) -> datetime.timedelta:
    return calculate_pushtime(button_pressings) / len(button_pressings)

def calculate_pushtime(button_pressings: list) -> datetime.timedelta:
    pushtime: datetime.timedelta = datetime.timedelta()

    for press in button_pressings:
        # Position 2 ist die Druckdauer, die drückzeit wird aus allen in der Liste enthaltenen Zeiten zusammengerechnet.
        pushtime += datetime.timedelta.st press[2]

    return pushtime

if __name__ == "__main__":
    send_daily_update()