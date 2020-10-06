# -*- coding: utf-8 -*-
import re
import requests
import base64
import time
import datetime
from urllib import parse
from bs4 import BeautifulSoup
import telebot
import os



# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']

session = requests.session()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['saucenao'])
def send_saucenao(message):
    bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")
    bot.register_next_step_handler(message, get_saucenao)

def get_saucenao(message):
    print(message)

    if message.text=="/cancel":
        bot.send_message(chat_id=message.chat.id, text="已退出搜图模式", parse_mode="MarkdownV2")
        return
    if message.content_type!="photo":
        bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")

        bot.register_next_step_handler(message, get_ascii2d)
        return
    else:
        url = bot.get_file_url(message.photo[-1].file_id)
        print(url)
        saucenao(url, message.chat.id)
        bot.send_message(chat_id=message.chat.id, text="搜索完成", parse_mode="MarkdownV2")



@bot.message_handler(commands=['ascii2d'])
def send_ascii2d(message):
    bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")
    bot.register_next_step_handler(message, get_ascii2d)

def get_ascii2d(message):
    print(message)
    if message.text=="/cancel":
        bot.send_message(chat_id=message.chat.id, text="已退出搜图模式", parse_mode="MarkdownV2")
        return
    if message.content_type!="photo":
        bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")

        bot.register_next_step_handler(message, get_ascii2d)
        return
    else:
        url = bot.get_file_url(message.photo[-1].file_id)
        print(url)
        ascii2d(url, message.chat.id)
        bot.send_message(chat_id=message.chat.id, text="搜索完成", parse_mode="MarkdownV2")

@bot.message_handler(commands=['anime'])
def send_anime(message):
    bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")
    bot.register_next_step_handler(message, get_anime)

def get_anime(message):
    print(message)
    if message.text=="/cancel":
        bot.send_message(chat_id=message.chat.id, text="已退出搜图模式", parse_mode="MarkdownV2")
        return
    if message.content_type!="photo":
        bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")

        bot.register_next_step_handler(message, get_ascii2d)
        return
    else:
        url = bot.get_file_url(message.photo[-1].file_id)
        print(url)
        anime(url, message.chat.id)
        bot.send_message(chat_id=message.chat.id, text="搜索完成", parse_mode="MarkdownV2")

@bot.message_handler(commands=['iqdb'])
def send_iqdb(message):
    bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")
    bot.register_next_step_handler(message, get_iqdb)

def get_iqdb(message):
    print(message)
    if message.text=="/cancel":
        bot.send_message(chat_id=message.chat.id, text="已退出搜图模式", parse_mode="MarkdownV2")
        return
    if message.content_type!="photo":
        bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")

        bot.register_next_step_handler(message, get_ascii2d)
        return
    else:
        url = bot.get_file_url(message.photo[-1].file_id)
        print(url)
        iqdb(url, message.chat.id)
        bot.send_message(chat_id=message.chat.id, text="搜索完成", parse_mode="MarkdownV2")


@bot.message_handler(commands=['all'])
def send_all(message):
    bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")
    bot.register_next_step_handler(message, get_all)

def get_all(message):
    print(message)
    if message.text=="/cancel":
        bot.send_message(chat_id=message.chat.id, text="已退出搜图模式", parse_mode="MarkdownV2")
        return
    if message.content_type!="photo":
        bot.send_message(chat_id=message.chat.id, text="请发送图片,或输入 /cancel 取消",parse_mode="MarkdownV2")

        bot.register_next_step_handler(message, get_ascii2d)
        return
    else:
        url = bot.get_file_url(message.photo[-1].file_id)
        print(url)
        saucenao(url, message.chat.id)
        ascii2d(url, message.chat.id)
        anime(url, message.chat.id)
        iqdb(url, message.chat.id)
        bot.send_message(chat_id=message.chat.id, text="搜索完成", parse_mode="MarkdownV2")

def saucenao(photo_url,chat_id):
    try:
        url="https://saucenao.com/search.php"
        #url = "https://saucenao.com"
        Header = {
            'Host': 'saucenao.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
             'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8',
            'Accept - Language': 'zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
             'Accept - Encoding': 'gzip, deflate, br',
            'Connection': 'keep - alive',

        }
        payloaddata = {

            'frame': 1,
            'hide': 0,
            'database': 999,
        }
        #files = {"file": "file": ('saber.jpg', open("saber.jpg", "rb", , "image/png")}
        photo_file=requests.get(photo_url)
        files = {"file": (
        "saucenao.jpg", photo_file.content, "image/png")}
        bot.send_message(chat_id=chat_id,text="正在搜索saucenao")
        r = session.post(url=url, headers=Header, data=payloaddata,files=files)
        #r = session .get(url=url,headers=Header)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.prettify())
        result=0
        choice=0
        for img in soup.find_all('div', attrs={'class': 'result'}):  # 找到class="wrap"的div里面的所有<img>标签
            #print(img)
            if('hidden' in str(img['class']))==False:
                try:
                    name=img.find("div",attrs={'class': 'resulttitle'}).get_text()
                    img_url=str(img.img['src'])
                    describe_list=img.find("div",attrs={'class': 'resultcontentcolumn'})
                    url_list = img.find("div", attrs={'class': 'resultcontentcolumn'}).find_all("a",  attrs={'class': 'linkify'})
                    similarity = str(img.find("div", attrs={'class': 'resultsimilarityinfo'}).get_text())
                    print(name)
                except:
                    continue
                try:
                    describe = str(url_list[0].previous_sibling.string)
                    describe_id = str(url_list[0].string)
                    describe_url = str(url_list[0]['href'])
                    auther_url = str(url_list[1]['href'])
                    auther = str(url_list[1].previous_sibling.string)
                    auther_id = str(url_list[1].string)
                    '''print(name)
                    print(img_url)
                    print(describe)
                    print(describe_id)
                    print(similarity)
                    print(auther)
                    print(auther_id)
                    print(describe_url)'''
                    text = f"{name}\n{describe}[{describe_id}]({describe_url})\n{auther}:[{auther_id}]({auther_url})\n相似度{similarity}"
                except:
                    '''print(describe_list.get_text())
                    print(describe_list.strong.string)
                    print(describe_list.strong.next_sibling.string)
                    print(describe_list.small.string)
                    print(describe_list.small.next_sibling.next_sibling.string)'''
                    auther = str(describe_list.strong.string)
                    auther_id = str(describe_list.strong.next_sibling.string)
                    describe = str(describe_list.small.string) + "\n" + str(describe_list.small.next_sibling.next_sibling.string)
                    text = f"{name}\n{auther}:{auther_id}\n{describe}\n相似度{similarity}"

                photo_file = session.get(img_url)
                bot.send_photo(chat_id=chat_id,photo=photo_file.content,parse_mode='Markdown',caption=text)


                result=1
        if result==0:
            bot.send_message(chat_id=chat_id, text="saucenao无结果")
    except:
        print("saucenao")

def ascii2d(photo_url,chat_id):
    try:
        url = "https://ascii2d.net/"
        # url = "https://saucenao.com"
        Header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        }
        html = session.get(url, headers=Header)
        print(html)
        authenticity_token = re.findall("<input type=\"hidden\" name=\"authenticity_token\" value=\"(.*?)\" />", html.text, re.S)[0]
        payloaddata = {

            'authenticity_token': authenticity_token,
            'utf8': "✓",
        }
        # files = {"file": "file": ('saber.jpg', open("saber.jpg", "rb", , "image/png")}
        bot.send_message(chat_id=chat_id, text="正在搜索ascii2d")
        photo_file = requests.get(photo_url)
        files = {"file": (
            "saucenao.jpg", photo_file.content, "image/png")}
        url = "https://ascii2d.net/search/multi"
        r = session.post(url=url, headers=Header, data=payloaddata, files=files)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup.prettify())
        pan = 0
        for img in soup.find_all('div', attrs={'class': 'row item-box'}):  # 找到class="wrap"的div里面的所有<img>标签
            # print(img)
            if pan != 0:
                img_url = "https://ascii2d.net" + str(img.img['src'])
                the_list = img.find_all('a')
                title = str(the_list[0].get_text())
                title_url = str(the_list[0]["href"])
                auther = str(the_list[1].get_text())
                auther_url = str(the_list[1]["href"])

                photo_file = session.get(img_url)
                text=f"titile:[{title}]({title_url})\nauther:[{auther}]({auther_url})"
                bot.send_photo(chat_id=chat_id, caption=text, parse_mode='Markdown',photo=photo_file.content)
            pan = pan + 1
            if pan == 3:
                break
    except:
        print("ascii2d faild")


def anime(photo_url,chat_id):
    try:
        url = "https://trace.moe/api/search"
        # url = "https://saucenao.com"
        photo_file = requests.get(photo_url)
        ls_f = base64.b64encode(photo_file.content)

        data = {
            "image": ls_f,
        }
        # files = {"file": "file": ('saber.jpg', open("saber.jpg", "rb", , "image/png")}

        r = session.post(url=url, data=data)
        # r = session .get(url=url,headers=Header)
        bot.send_message(chat_id=chat_id,text="正在搜索 trace.moe")
        information = r.json()
        anilist_id = information['docs'][0]["anilist_id"]
        filename = information['docs'][0]['filename']
        tokenthumb = information['docs'][0]['tokenthumb']
        at = information['docs'][0]['at']
        limit = information['limit']  # 剩余搜索次数
        limit_ttl = information['limit_ttl']  # 剩余重置时间
        title = information['docs'][0]['title_chinese']
        episode = information['docs'][0]['episode']
        quota = information['quota']
        quota_ttl = information['quota_ttl']
        similarity=information['docs'][0]['similarity']
        similarity_num="%.2f%%" % (similarity * 100)
        img_url = f"https://trace.moe/thumbnail.php?anilist_id={anilist_id}&file={parse.quote(filename)}&t={at}&token={tokenthumb}"
        print(img_url)
        video_url = f"https://trace.moe/preview.php?anilist_id={anilist_id}&file={parse.quote(filename)}&t={at}&token={tokenthumb}"
        print(video_url)
        video = f"https://media.trace.moe/video/{anilist_id}/{parse.quote(filename)}?t={at}&token={tokenthumb}"
        print(video)
        more_url = f"https://anilist.co/anime/{anilist_id}"
        text = f"{similarity_num}\nTitle:{title}\n集数:{episode}\n时间：{datetime.timedelta(seconds=int(at))}\n来源：{filename}\n[更多信息]({more_url})\n分钟剩余搜索次数:{limit}\n分钟剩余次数重置时间:{limit_ttl}s\n24小时剩余搜索次数:{quota}\n24小时剩余次数重置时间:{datetime.timedelta(seconds=int(quota_ttl))}"
        print(text)
        photo_file = session.get(img_url)
        bot.send_photo(chat_id=chat_id, photo=photo_file.content, parse_mode='Markdown', caption=text)
        photo_file = session.get(video)
        bot.send_video(chat_id=chat_id,data=photo_file.content)
    except:
        print("anime faild")

def iqdb(photo_url,chat_id):
    try:
        bot.send_message(chat_id=chat_id, text="正在搜索 iqdb", parse_mode="MarkdownV2")
        url = "http://iqdb.org/"
        # url = "https://saucenao.com"
        photo_file = requests.get(photo_url)
        files = {"file": (
            "iqdb.jpg", photo_file.content, "image/png")}
        # files = {"file": "file": ('saber.jpg', open("saber.jpg", "rb", , "image/png")}

        r = requests.post(url=url, files=files)
        #print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=1
        for img in soup.find_all('td', attrs={'class': 'image'}):  # 找到class="wrap"的div里面的所有<img>标签
            #print(img)
            if a==7:
                break
            try:
                #print(img.a.get('href'))
                img_html=img.a.get('href')
                if "http:" not in img_html and "https:" not in img_html:

                    img_html="https:"+img_html

                img_url="http://iqdb.org"+img.img.get('src')

                text=f"[图片详情]({img_html})"
                photo_file = session.get(img_url)
                bot.send_photo(chat_id=chat_id, photo=photo_file.content, parse_mode='Markdown', caption=text)
                a=a+1
            except:
                None
    except:
        None

'''@bot.message_handler(content_types=['photo'])
def get_photo(message):
    #print(message)
    #print(message.photo[-1].file_id)
    #bot.get_file_url
    url=bot.get_file_url(message.photo[-1].file_id)
    print(url)
    saucenao(url,message.chat.id)
    ascii2d(url, message.chat.id)
    anime(url, message.chat.id)'''





if __name__ == '__main__':

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(2)

