#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Title         : mpd-rfid.py
Author        : zzeromin member of Tentacle Team
Creation Date : June 6, 2019
Cafe          : http://cafe.naver.com/raspigamer, https://cafe.naver.com/unclejump, https://cafe.naver.com/doksumaker
Thanks to     : Tentacle Team, Raspigamer, MASIL, Doksumaker Cafe
Special thanks to : rolex member of Tentacle Team, you inspire me :)
Notice        :
MPD-RFID run on RuneAudio and MoodeAudio, a custom built GNU Linux operating system for Raspberry Pi.
installed python package: mfrc522
Free and open for all to use. But put credit where credit is due.
"""

import os
import time
import RPi.GPIO as GPIO
import dataswap
from mfrc522 import SimpleMFRC522

# Raspberry Pi pin configuration:
piezo = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(piezo, GPIO.OUT)

# RFID tags and information
duplication = True # check whether RFID recognizes duplicate cards
mpc_commands = {"next", "prev", "toggle", "stop", "vol+10", "vol-10"}
tag_list = {"album", "artist", "title", "track", "name", "genre", "date", "composer", "performer", "disc"}

def mpdControl(tag, card):
    os.system("mpc clear")
    if tag in tag_list:
        if tag == "playlist":
            os.system("mpc load " + card)
        else:
            os.system("mpc search " + tag + " " + card + " | mpc add; mpc play")
    os.system("mpc play")

def piezoBeep():
    piezo_pwm = GPIO.PWM(piezo, 2000)
    piezo_pwm.start(50)
    time.sleep(0.01)
    piezo_pwm.stop()

# main code
def main():
    reader = SimpleMFRC522()
    card = ""
    oldCard = ""

    while True:
        id, card = reader.read()
        card = card.replace(" ", "")
        card = card.lower()
        print("read.card = " + card)

        tag = card[0:3] # parse tag value in rfid card
        tag = dataswap.tagSwap(tag)

        if card in mpc_commands:
            os.system("mpc " + card)

        elif tag in tag_list:
            card = card[4:] # parse card value in rfid card
            card = dataswap.cardSwap(card)
            print("art.card = "+ card)

            if duplication:
                piezoBeep()
                mpdControl(tag, card)
                oldCard = card
                
            else:
                if oldCard != card:
                    piezoBeep()
                    mpdControl(tag, card)
                    oldCard = card
                    print("oldcard = "+ oldCard)

        else:
            pass

        card = ""
        time.sleep(1)

if __name__ == "__main__":
    import sys

    try:
        main()

    # Catch all other non-exit errors
    except Exception as e:
        sys.stderr.write("Unexpected exception: %s" % e)
        sys.exit(1)

    # Catch the remaining exit errors
    except:
        sys.exit(0)
