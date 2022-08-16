import RPi.GPIO as GPIO
import time
from bottle import route, run, template
import pigpio

#from gpiozero import Servo
from time import sleep

pi = pigpio.pi()
#servo = Servo(25)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)
# GPIO.output(3, False)   
    
@route('/LOCK/:lockstate')
def locktrigger(lockstate=0):
    if lockstate == '0':
        # GPIO.output(3, False)
        
        # CLOSE LOCK
        pi.set_servo_pulsewidth(25, 500)
        
        return 'LOCK CLOSED'
    elif lockstate == '1':
        # GPIO.output(3, True)
        
        # OPEN LOCK
        pi.set_servo_pulsewidth(25, 2500)
        
        return 'LOCK OPEN'

run(host='192.168.50.149', port=8081)
