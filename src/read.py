#!/usr/bin/env python
# Reading with the RFID RC522
# reference: https://pimylifeup.com/raspberry-pi-rfid-rc522/

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Hold a tag near the reader")
    id, text = reader.read()
    #print(id)
    print("Card Name = " + text)
finally:
    GPIO.cleanup()
