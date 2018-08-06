#!/usr/bin/python

import paho.mqtt.client as mqtt
import json
import logging

logging.basicConfig(filename='voltlog.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def on_connect(client, userdata, flags, rc):
	client.subscribe("tele/sonoffpow/ENERGY")

def on_message(client, userdata, msg):
	bruto = msg.payload
	carga = json.loads(bruto)
	volts = carga['Voltage']
	print(volts)
	logging.info(volts)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.0.0.254", 1883, 60)

try:
	client.loop_forever()

except KeyboardInterrupt:
	print("Exiting")

