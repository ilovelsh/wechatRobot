# coding=utf-8

from flask import Flask
from exts.itchatExt import itchat

from handler.wechatHandler import wechatHandler

app = Flask(__name__)

app.register_blueprint(wechatHandler, url_prefix='/wechatHandler')

if __name__ == '__main__':
    itchat.auto_login(True)
    app.run()