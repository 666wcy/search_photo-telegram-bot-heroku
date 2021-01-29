


from bot import *

import threading
from flask import Flask
status =""
app = Flask(__name__)

@app.route('/bot', methods=['GET'])
def bot_info():
    try:
        print(bot.get_me())
        return str(bot.get_me())
    except:
        return "无法获取bot信息，请检查api token"

def run_bot():

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(10)




@app.route('/', methods=['GET'])
def index():
    global status
    if status=="":
        t1 = threading.Thread(target=run_bot)  # 通过target指定子线程要执行的任务。可以通过args=元组 来指定test1的参数。

        t1.start()  # 只有在调用start方法后才会创建子线程并执行

        print(t1.is_alive())
        status=t1
        # threading.enumerate()  打印正在执行的线程,包括主线程和子线程
        #print(threading.enumerate())
        return "正在唤醒Bot", 200
    else:
        print(status.is_alive())
        if status.is_alive()==True:
            return "Bot 已经在运行", 200
        elif status.is_alive()==False:
            t1 = threading.Thread(target=run_bot)  # 通过target指定子线程要执行的任务。可以通过args=元组 来指定test1的参数。

            t1.start()  # 只有在调用start方法后才会创建子线程并执行

            print(t1.is_alive())
            status=t1
            return "重新唤醒Bot", 200

#worker: python3 bot.py

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)