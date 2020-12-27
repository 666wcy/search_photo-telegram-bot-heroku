# TelegramBot

一个聚合搜索图片的tg机器人,支持部署在heroku上。

目前支持的网站：

[saucenao](https://saucenao.com/)

[WhatAnime](https://trace.moe/)

[ascii2d](https://ascii2d.net/)

[iqdb](http://www.iqdb.org/)



**安装方法:**

登录heroku账号,后点击下面的按钮;若浏览器中已登录heroku则直接点击

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)



安装教程：[搜图机器人](http://weinb.top/index.php/archives/93/)

docker版

```
docker run  --name search -d \
-e TELEGRAM_TOKEN=你机器人的API \
--restart=always \
benchao/search-photo:1.1

```





Botfather命令设置

```
iqdb-在iqdb搜索
ascii2d-在ascii2d搜索
anime-番剧截图搜索
saucenao-在saucenao搜索，pixiv，本子
all-搜索全部选项
week-pixiv周榜
day-pixiv日榜
month-pixiv月榜
```



项目灵感:[CQ-picfinder-robot](https://github.com/Tsuk1ko/CQ-picfinder-robot)

感谢：[TelegramBot](https://github.com/akashin/TelegramBot)