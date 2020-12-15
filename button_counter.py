from mailsender import send_mail
from gpiozero import Button
import datetime
import databasemanager
import mailsender
import settings_reader
import signal


press_start: datetime.datetime
press_end: datetime.datetime


def run_loop() -> None:


    pin_to_read: int = settings_reader.get_pin_to_read()
    batch_wait_time: int = settings_reader.get_batch_send_wait_time()

    # Erstellen eines Knopfobjektes
    button: Button = Button(pin_to_read)

    button.when_pressed = button_press
    button.when_released = button_release
    signal.pause()


def button_press() -> None:
    global press_start 
    press_start = datetime.datetime.now()
    

def button_release() -> None:
    global press_start

    press_end = datetime.datetime.now()

    databasemanager.add_button_press(press_start, press_end-press_start)
    send_button_press(press_start, press_end-press_start)


def send_button_press(press_start: datetime.datetime, press_duration: datetime.timedelta) -> None:

    # Formatiert das Datum nach der im mailsender gegebenen Formatierung
    date = press_start.strftime(mailsender.DATE_FORMAT)

    # Formatiert die Sekunden und Microsekunden nach dem im mailsender gegebenen Formatierung
    duration = mailsender.format_seconds(press_duration.seconds, press_duration.microseconds)

    subject = "Der Knopf wurde gedrückt!"
    message = "Am {0} wurde der Knopf für {1} Sekunden gedrückt!".format(date, duration)

    mailsender.send_mail(subject, message)


if __name__ == "__main__":
    run_loop()