#!/usr/bin/python

import urllib2
import os
import glob
import time
from decimal import Decimal
# If you also want to send temp updates to an MQTT server like Mosquito
import paho.mqtt.client as mqtt  # import the client1

import simplejson as json

# You will need to have installed these modules for the DS18B20
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
# Your Dallas 1wire device path
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
# Your MQTT host to deliver temps to
broker_address = "mqtt.yourmqtthost.com"


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_c = Decimal(temp_c)
        temp_c = round(temp_c, 2)
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        temp_f = round(temp_f, 2)
        # Push the celcius temp to the default admin port of the motioneye using your password
        url = "wget -q --delete-after http://admin:ADMINPASSWORD@localhost:7999/1/config/set?text_left=" + str(temp_c)
        result = os.system(url)
        # return temp_c, temp_f
        client = mqtt.Client("P1")  # create new instance
        client.tls_set('/etc/ssl/certs/ca-certificates.crt')
        # mqtt user and password
        client.username_pw_set('temp', 'PASSWORD')
        # MQTT host port
        client.connect(broker_address, port=8883)  # connect to broker
        message = {
            'temp_c': temp_c,
        }
        # MQTT Topic
        client.publish("pi/temp_c", payload=json.dumps(message))  # publish
        # STDOUT
        print
        temp_c
        print
        temp_f


read_temp()
exit
# while True:
#	print(read_temp())
#	time.sleep(1)