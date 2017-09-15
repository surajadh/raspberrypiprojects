from flask import Flask
from flask import make_response

import RPi.GPIO as GPIO

YELLOW = 17
GREEN = 0       //TODO change this
RED = 0         //TODO change this

GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOW, GPIO.OUT)

app = Flask(__name__)

@app.route("/on/<light>")
def turnon(light):
        if !light
                return make_response('No Light specified')
        if light == 'yellow':
                GPIO.output(YELLOW, 1)
                return make_response(light + ' is on')
        elif light == 'red':
                GPIO.output(RED, 1)
                return make_response(light + ' is on')
        elif light == 'green':
                GPIO.output(GREEN, 1)
                return make_response(light + ' is on')
        else:
                return make_response('Selected Light is not available in explorer pro')
            

@app.route("/off/<light>")
def turnoff(light):
        if !light
                return make_response('No Light specified')
        if light == 'yellow':
                GPIO.output(YELLOW, 0)
                return make_response(light + ' is off')
        elif light == 'red':
                GPIO.output(RED, 0)
                return make_response(light + ' is off')
        elif light == 'green':
                GPIO.output(GREEN, 0)
                return make_response(light + ' is off')
        else:
                return make_response('Selected Light is not available in explorer pro')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug = True)