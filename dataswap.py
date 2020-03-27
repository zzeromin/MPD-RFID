#!/usr/bin/env python
# -*- coding: utf-8 -*-

def artistSwap(card):
    artistMap = {
        ### 데이터 추가 방법 ###
        ### "카드명":"한글가수명", ###
        "bts":"방탄소년단",
        "bol4":"볼빨간사춘기",
        "psy":"싸이",
        "cool":"쿨",
    }
    return artistMap.get(card, card)

def tagSwap(tag):
    tagMap = {
        "alb":"album",
        "art":"artist",
        "pla":"playlist",
        "tit":"title",
        "com":"command",
    }
    return tagMap.get(tag, tag)
