import RPi.GPIO as GPIO
import time
from bottle import route, run, template

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, False)   

@route('/LED/:ledstate')
def ledtrigger(ledstate=0):
    if ledstate == '0':
        GPIO.output(3, False)
        return 'LED OFF'
    elif ledstate == '1':
        GPIO.output(3, True)
        return 'LED ON'
    
@route('/LOCK/:lockstate')
def locktrigger(lockstate=0):
    if lockstate == '0':
        GPIO.output(3, False)
        # CLOSE LOCK
        return 'LED OFF'
    elif lockstate == '1':
        GPIO.output(3, True)
        # OPEN LOCK
        return 'LED ON'

run(host='192.168.50.149', port=8081)
