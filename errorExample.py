#! python3
# coding: utf-8

def spam():
    bacon()

def bacon():
    raise Exception('これはエラーメッセージです。')

spam()