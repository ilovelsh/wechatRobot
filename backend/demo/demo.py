# coding=utf-8

import itchat

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 1、send hello to filehelper
# itchat.send('hello filehelper', toUserName='filehelper')


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print msg.fromUserName
    print msg.type
    print msg.text
    return msg.text


def getFriends():
    friends = itchat.get_friends(update=True)[0:]
    print len(friends)


def getGroups():
    groups = itchat.get_chatrooms(update=True)
    print len(groups)
    print groups[0]
    # 显示所有的群聊，包括未保存在通讯录中的，如果去掉则只是显示在通讯录中保存的
    itchat.dump_login_status()


if __name__ == '__main__':
    itchat.auto_login()
    getFriends()
    getGroups()
    itchat.run(True)
