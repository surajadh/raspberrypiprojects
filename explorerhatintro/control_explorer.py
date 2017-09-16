from flask import Flask
from flask import render_template

import RPi.GPIO as GPIO

YELLOW = 17
GREEN = 4
RED = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
@app.route("/<light>/on/")
def turnon(light = None):
        if not light:
                return render_template('explorer_button_template.html', message = 'No Light specified')
        if light == 'yellow':
                GPIO.output(YELLOW, 1)
                return render_template('explorer_button_template.html', message = light + ' is on')
        elif light == 'red':
                GPIO.output(RED, 1)
                return render_template('explorer_button_template.html', message = light + ' is on')
        elif light == 'green':
                GPIO.output(GREEN, 1)
                return render_template('explorer_button_template.html', message = light + ' is on')
        else:
                return render_template('explorer_button_template.html', \
        message = 'Selected Light is not available in explorer pro')
            

@app.route("/<light>/off/")
def turnoff(light):
        if not light or light.isspace():
                return render_template('explorer_button_template.html', message = 'No Light specified')
        if light == 'yellow':
                GPIO.output(YELLOW, 0)
                return render_template('explorer_button_template.html', message = light + ' is off')
        elif light == 'red':
                GPIO.output(RED, 0)
                return render_template('explorer_button_template.html', message = light + ' is off')
        elif light == 'green':
                GPIO.output(GREEN, 0)
                return render_template('explorer_button_template.html', message = light + ' is off')
        else:
                return render_template('explorer_button_template.html', \
        message = 'Selected Light is not available in explorer pro')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug = True)