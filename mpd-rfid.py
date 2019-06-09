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
MPD-RFID runs on RuneAudio and MoodeAudio, a custom built GNU Linux operating system for Raspberry Pi.
installed python package: mfrc522
Free and open for all to use. But put credit where credit is due.
"""

import os
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# setup piezo
piezo = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo, GPIO.OUT)

# rfid tags and information
mpc_commands = {"next", "prev", "toggle", "stop", "vol+10", "vol-10"}
tag_list = {"album", "artist", "title", "track", "name", "genre", "date", "composer", "performer", "disc"}

def tagSwap(tag):
    if tag == "alb":   # alb = album
        tag = "album"
    elif tag == "art": # art = artist
        tag = "artist"
    elif tag == "pla": # pla = playlist
        tag = "playlist"
    elif tag == "tit": # tit = title
        tag = "title"
    elif tag == "com": # com = command
        tag = "command"
    return tag

def artistSwap(card):
    artistMap = {
        ### 데이터 추가 방법 ###
        ### "카드명":"한글가수명", ###
        "bts":"방탄소년단",
        "bol4":"볼빨간사춘기",
        "psy":"싸이",
    }
    card = artistMap.get(card, card)

def mpdControl(tag, card):
    artistSwap(card)

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
reader = SimpleMFRC522()

while True:

    id, card = reader.read()
    card = card.replace(" ", "")
    piezoBeep()

    tag = card[0:3] # parse tag value in rfid card
    tag = tagSwap(tag)
    #print("card = " + card)
    #print("tag = " + tag)

    if card in mpc_commands:
        os.system("mpc " + card)

    elif tag in tag_list:
        card = card[4:] # parse card value in rfid card
        mpdControl(tag, card)

    else:
        pass

    card = ""
    time.sleep(1)
