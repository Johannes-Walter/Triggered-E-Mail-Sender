import RPi.GPIO as GPIO
imprt datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

press_start as datetime.datetime
press_end as datetime.datetime


print("programm starting")
while True:
    if GPIO.input(10) == GPIO.HIGH:
        press_start = datetime.datetime.now()
        while GPIO.input(10) == GPIO.HIGH:
            pass
        press_end = datetime.datetime.now()
        