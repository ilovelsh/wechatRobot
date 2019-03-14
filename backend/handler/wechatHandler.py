# coding=utf-8

from flask import Blueprint, jsonify, request
from exts.itchatExt import itchat

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