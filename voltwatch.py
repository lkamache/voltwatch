#!/usr/bin/python

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	client.subscribe("tele/sonoffpow/ENERGY")

def on_message(client, userdata, msg):
	bruto = msg.payload
	print(bruto)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.0.0.254", 1883, 60)

try:
	client.loop_forever()

except KeyboardInterrupt:
	print("Exiting")

