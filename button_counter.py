import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("programm starting")
while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed")
        while GPIO.input(10) == GPIO.HIGH:
            pass
        print("Button was realeased")