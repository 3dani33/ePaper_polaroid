import RPi.GPIO as GPIO

BUTTON_PIN = 4

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if __name__ == '__main__':
    setup()
    while True:
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING)
        print('button!')