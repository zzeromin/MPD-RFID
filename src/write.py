#!/usr/bin/env python
# Writing with the RFID RC522
# reference: https://pimylifeup.com/raspberry-pi-rfid-rc522/

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Hold a tag near the reader")
    text = input('New data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")
finally:
    GPIO.cleanup()
