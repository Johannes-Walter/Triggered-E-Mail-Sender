from mailsender import send_mail
import RPi.GPIO as GPIO
import datetime
import databasemanager
import mailsender
import settings_reader
import time

def run_loop() -> None:

    press_start: datetime.datetime
    press_end: datetime.datetime
    pin_to_read: int = settings_reader.get_pin_to_read()
    batch_wait_time: int = settings_reader.get_batch_send_wait_time()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_to_read, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("GPIO_loop starting...")
    while True:
        # Auf das Betätigen des Knopfes warten
        GPIO.wait_for_edge(pin_to_read, GPIO.RISING)
        press_start = datetime.datetime.now()
        # Knopf entprellen
        time.sleep(0.05)

        # Auf das Loslassen des Knopfes Warten
        GPIO.wait_for_edge(pin_to_read, GPIO.FALLING)
        press_end = datetime.datetime.now()
        # Knopf entprellen
        time.sleep(0.05)

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