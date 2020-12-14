from typing import get_args
from mailsender import send_mail
import RPi.GPIO as GPIO
import datetime
import databasemanager
import mailsender


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

press_start: datetime.datetime
press_end: datetime.datetime


def GPIO_loop():
    print("GPIO_loop starting...")
    while True:
        if GPIO.input(10) == GPIO.HIGH:
            press_start = datetime.datetime.now()
            while GPIO.input(10) == GPIO.HIGH:
                pass
            press_end = datetime.datetime.now()

            databasemanager.add_button_press(press_start, press_end-press_start)
            send_button_press(press_start, press_end-press_start)


def send_button_press(press_start: datetime.datetime, press_duration: datetime.timedelta):

    # Formatiert das Datum nach der im mailsender gegebenen Formatierung
    date = press_start.strftime(mailsender.DATE_FORMAT)

    # Formatiert die Sekunden und Microsekunden nach dem im mailsender gegebenen Formatierung
    duration = mailsender.format_seconds(press_duration.seconds, press_duration.microseconds)

    subject = "Der Knopf wurde gedrückt!"
    message = "Am {0} wurde der Knopf für {1} Sekunden gedrückt!".format(date, duration)

    mailsender.send_mail(subject, message)

