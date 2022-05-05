# -*- coding: utf-8 -*-

import telebot
from telebot import apihelper
import sys
import datetime
import time
def log(message):
    file_name = '/root/log/log.txt'
    file3 = open(file_name,'a')
    file3.write(str(datetime.datetime.now())+' '+str(message)+'\n')
    file3.close()
for er in range(0,8):
       try:
                token = "you key"
                bot = telebot.TeleBot(token)
#                apihelper.proxy = {'https': 'socks5://207.97.174.134:1080'}
                bot.send_message(-317729700, 'Критическое сообщение:\n'+ sys.argv[2] +'\n'+
                                '__________________________\n'+

                                'Время регистрации:\n'+sys.argv[1] +'\n'+

                                'На каком Оборудовании:\n'+ sys.argv[3] +'\n'+

                                'На какой Площадке:\n' +sys.argv[4] +'\n'+

                                'Какой район:\n'+ sys.argv[5] +'\n'+

                                'IP Адрес\n'+sys.argv[6]+'\n'+

                                '__________________________\n')
                break
       except Exception as e:
               msg = ' '.join(sys.argv[1:])
               log(msg)
               print (str(e))
               time.sleep(3)
