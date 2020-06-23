#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MPD-RFID Data(TAG) online sheet
# https://bit.ly/3dBzLv0

def cardSwap(card):
    dataMap = {
        ### 데이터 추가 방법 ###
        ### "카드명":"한글가수명", ###
        "iu":"아이유",
        "bts":"방탄소년단",
        "redvelvet":"레드벨벳",
        "bol4":"볼빨간사춘기",
        "psy":"싸이",
        "cool":"쿨",
        "apink":"에이핑크",
        "taeyeon":"태연",
        "twice":"트와이스",
        "mamamoo":"마마무",
        "izone":"아이즈원",
        "sejeong":"세정",
    }
    return dataMap.get(card, card)

def tagSwap(tag):
    tagMap = {
        "alb":"album",
        "art":"artist",
        "pla":"playlist",
        "tit":"title",
        "com":"command",
        "utu":"utube",
    }
    return tagMap.get(tag, tag)

def utubeSwap(utube):
    utubeMap = {
        "on":"mpc stop; sudo -u pi DISPLAY=:0 chromium-browser --start-fullscreen --app=https://youtube.com/watch?v=1oGHSDyDEqA&feature=share?autoplay=1",
        "off":"export DISPLAY=:0; xdotool key Ctrl+Shift+w",
    }
    return utubeMap.get(utube, utube)
