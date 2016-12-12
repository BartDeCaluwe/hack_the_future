import time
import grovepi
import math

import sys
from flask import Flask, abort, jsonify, request
import random

app = Flask(__name__)

from datetime import timedelta  
from flask import make_response, current_app  
from functools import update_wrapper


webserverIp = "0.0.0.0"


# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
def panicButton():
    button = 2

    grovepi.pinMode(button, "INPUT")
    try:
        return grovepi.digitalRead(button)
        time.sleep(.5)

    except IOError:
        print ("Error")

def lightSensor():
    light_sensor = 0

    # Connect the LED to digital port D6
    # SIG,NC,VCC,GND
    led = 6

    # Turn on LED once sensor exceeds threshold resistance
    threshold = 10

    grovepi.pinMode(light_sensor,"INPUT")
    grovepi.pinMode(led,"OUTPUT")

    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        if resistance > threshold:
            # Send HIGH to switch on LED
            grovepi.digitalWrite(led,1)
        else:
            # Send LOW to switch off LED
            grovepi.digitalWrite(led,0)

        return (sensor_value, resistance)
        time.sleep(.5)

    except IOError:
        print ("Error")


def soundSensor():
    # Connect the Grove Sound Sensor to analog port A0
    # SIG,NC,VCC,GND
    sound_sensor = 0

    # Connect the Grove LED to digital port D3
    # SIG,NC,VCC,GND
    led = 3

    grovepi.pinMode(sound_sensor,"INPUT")
    grovepi.pinMode(led,"OUTPUT")

    # The threshold to turn the led on 400.00 * 5 / 1024 = 1.95v
    threshold_value = 400
    try:
        # (20 * log10(value + 1) ).
        # Read the sound level
        sensor_value = 20 * math.log10(grovepi.analogRead(sound_sensor) + 1)
        
        # If loud, illuminate LED, otherwise dim
        if sensor_value > threshold_value:
            grovepi.digitalWrite(led,1)
        else:
            grovepi.digitalWrite(led,0)

        return sensor_value
        time.sleep(.5)

    except IOError:
        print ("Error")

def temperatureSensor():
    sensor = 0
    try:
        temp= grovepi.temp(sensor,'1.1') - 273.15
        return(temp)
        time.sleep(.5)
    except IOError:
        print ("Error")
def ultrasoundDistanceSensor():
    ultrasonic_ranger = 4
    try:
        return (grovepi.ultrasonicRead(ultrasonic_ranger))
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")

def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):  
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/')
@crossdomain(origin='*')
def landing():  
    return jsonify(i_am_a='cross domain resource!')


@app.route('/getButtonState', methods=['GET'])
@crossdomain(origin='*')
def getButtonState():
    response = jsonify({'data': panicButton()}), 200
    return response

@app.route('/getLightState', methods=['GET'])
@crossdomain(origin='*')
def getLightState():
    response = jsonify({'data': lightSensor()}), 200
    return response

@app.route('/getSoundState', methods=['GET'])
@crossdomain(origin='*')
def getSoundState():
    response = jsonify({'data': soundSensor()}), 200
    return response

@app.route('/getTemperatureState', methods=['GET'])
@crossdomain(origin='*')
def getTemperatureState():
    response = jsonify({'data': temperatureSensor()}), 200
    return response

@app.route('/getUltrasoundDistanceState', methods=['GET'])
@crossdomain(origin='*')
def getUltrasoundDistanceState():
    response = jsonify({'data': ultrasoundDistanceSensor()}), 200
    return response

if __name__ == '__main__':
    app.run(debug=True,host=webserverIp)