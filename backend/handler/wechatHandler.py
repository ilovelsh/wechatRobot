# coding=utf-8

from flask import Blueprint, jsonify, request
from exts.itchatExt import itchat

from threading import Thread

from unit import *

wechatHandler = Blueprint('/wechatHandler', __name__)


@wechatHandler.route('/getFriends', methods=['POST'])
def getFriends():
    friends = itchat.get_friends(update=True)
    personList = []
    for f in range(1, len(friends)):
        person = {}
        if friends[f]['RemarkName']:
            userName = friends[f]['RemarkName']
        else:
            userName = friends[f]['NickName']
        sex = friends[f]['Sex']
        userId = friends[f]['UserName']
        person['userId'] = userId
        person['userName'] = userName
        person['sex'] = sex
        personList.append(person)

    return personList


@wechatHandler.route('/getGroups', methods=['POST'])
def getGroups():
    groups = itchat.get_chatrooms(update=True)
    groupList = []
    for g in groups:
        group = {}
        group['groupId'] = g['UserName']
        group['groupName'] = g['NickName']
        group['groupMemberCount'] = g['MemberCount']
        groupList.append(group)

    return groupList


@wechatHandler.route('/sendMsg', methods=['POST'])
def sendMsg():
    params = request.args
    userList = params.get('userList')
    textMsg = params.get('msg')
    for userid in userList:
        itchat.send(textMsg, userid)


@wechatHandler.route('/sendImage', methods=['POST'])
def sendImage():
    params = request.args
    userList = params.get('userList')
    path = params.get('imgPath')
    for userid in userList:
        itchat.send_image(path, userid)


@wechatHandler.route('/sendFile', methods=['POST'])
def sendFile():
    params = request.args
    userList = params.get('userList')
    path = params.get('filePath')
    for userid in userList:
        itchat.send_file(path, userid)


@wechatHandler.route('/sendVideo', methods=['POST'])
def sendVideo():
    params = request.args
    userList = params.get('userList')
    path = params.get('videoPath')
    for userid in userList:
        itchat.send_video(path, userid)


@wechatHandler.route('/getLoginStatus', methods=['POST'])
def getLoginStatus():
    return itchat.check_login()


thread = Thread()


@wechatHandler.route('/login', methods=['POST'])
def login():
    global thread
    uuid = itchat.get_QRuuid()
    itchat.get_QR(uuid=uuid, qrCallback=QR_to_b64)
    print(thread.is_alive())
    if thread.is_alive():
        return jsonify({'success': 0, 'msg': '已有登陆线程存在'})

    # thread = task(monitor_login,itchat)
    thread = Thread(target=monitor_login, args=(itchat, ))
    thread.start()
    return jsonify({'success': 1, 'qr': qr_b64.decode("utf-8")})
