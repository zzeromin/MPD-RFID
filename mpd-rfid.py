#!/usr/bin/env python3
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
installed python package: mfrc522, pi-rc522
Free and open for all to use. But put credit where credit is due.
"""

import os
import signal
import time
import sys
import RPi.GPIO as GPIO
import dataswap
from mfrc522 import SimpleMFRC522
from pirc522 import RFID

# Raspberry Pi pin configuration:
piezo = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(piezo, GPIO.OUT)

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

# RFID tags and information
duplication = True # check whether RFID recognizes duplicate cards
mpc_commands = {"next", "prev", "toggle", "stop", "vol+10", "vol-10"}
tag_list = {"album", "artist", "title", "playlist", "track", "name", "genre", "date", "composer", "performer", "disc"}
others = {"utube"}

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

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

# main code
def main():
    reader = SimpleMFRC522()
    card = ""
    oldCard = ""

    while run:
        rdr.wait_for_tag()

        (error, data) = rdr.request()
        if not error:
            print("\nDetected: " + format(data, "02x"))
            id, card = reader.read()
            card = card.replace(" ", "")
            card = card.lower()
            print("read.card = " + card)

            tag = card[0:3] # parse tag value in rfid card
            tag = dataswap.tagSwap(tag)
            print("tag =" + tag)

            if card in mpc_commands:
                os.system("mpc " + card)

            elif tag in others:
                card = card[6:] # parse card value in rfid card
                card = dataswap.utubeSwap(card)
                print("card = "+ card)
                os.system(card)

            elif tag in tag_list:
                card = card[4:] # parse card value in rfid card
                card = dataswap.cardSwap(card)
                print("card = "+ card)

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
