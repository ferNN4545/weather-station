'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 7-10-24
Developer FY
'''

#import libraries
import serial
import time

#Arduino port
arduino_port = 'COM5'
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout=1
)

time.sleep(1)#Delay
while True:
    #data = service.redline.decode('utf-8').strip()
    data = service.redline.decode('utf-8').rstrip()
    

    if data:
        print(data)
        #temperature, humidity = data.split(",")
        
        #print(f"Temperature: {temperature}°C")
        #print(f"Humidity: {humidity}%")
        
        
        
        #Here INSERT INTO
        
        #1. Create a new model data called test_data
        #Fields: id, temp, hum, created-at
        #2. Create a method
        
    time.sleep(1)
          
          
