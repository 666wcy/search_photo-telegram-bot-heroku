#!/bin/bash
wget -P / https://github.com/666wcy/seach_photo-telegram-bot-heroku/raw/master/bot.py
python bot.py
tail -f /dev/null	
