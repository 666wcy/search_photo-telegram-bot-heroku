import os

from flask import Flask
from bot import *

app = Flask(__name__)






@app.route('/', methods=['GET'])
def index():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(2)

    


#worker: python3 bot.py

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)