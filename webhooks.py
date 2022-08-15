import RPi.GPIO as GPIO
import time
from bottle import route, run, template

from gpiozero import Servo
from time import sleep

servo = Servo(25)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)
# GPIO.output(3, False)   
    
@route('/LOCK/:lockstate')
def locktrigger(lockstate=0):
    if lockstate == '0':
        GPIO.output(3, False)
        
        # CLOSE LOCK
        
        return 'LOCK CLOSED'
    elif lockstate == '1':
        GPIO.output(3, True)
        
        # SERVO
        servo.min()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.max()
        sleep(0.5)
        
        return 'LOCK OPEN'

run(host='192.168.50.149', port=8081)
