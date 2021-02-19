import paho.mqtt.client as mqtt 
import time
import random
broker_address="io.adafruit.com"
clientId="Joshtein Publish" 
ADAFRUIT_IO_USERNAME = "Joshtein"
ADAFRUIT_IO_KEY = "aio_Zmqv79FOAkDSSaz5Kuzxo0cZTvir"
topic = "Test"
topic_1 = "Sensor Suhu" 
topic_2 = "Sensor Kelembaban"

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("WPC DAY 3") #create new instance
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect(broker_address) #connect to broker
t = random.uniform(27.00, 33.00)
k = random.uniform(65.00, 85.00)

while True:
    #publish
    client.publish(ADAFRUIT_IO_USERNAME+"/feeds/"+topic,"OFF")
    client.publish(ADAFRUIT_IO_USERNAME+"/feeds/"+topic_1,t)
    client.publish(ADAFRUIT_IO_USERNAME+"/feeds/"+topic_2,k)
    time.sleep(1800)