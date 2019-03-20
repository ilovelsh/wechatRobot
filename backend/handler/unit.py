# coding=utf-8

import base64

qr_b64 = ""


def QR_to_b64(uuid, status, qrcode):
    global qr_b64
    qr_b64 = base64.b64encode(qrcode)
    return qr_b64
# 监控登陆状态 初始化


def monitor_login(itchat):
    isLoggedIn = False
    while 1:
        waiting_time = 0
        while not isLoggedIn:
            status = itchat.check_login()
            waiting_time += 1
            print(waiting_time)
            if status == '200':
                print ("status is 200!")
                isLoggedIn = True
            elif status == '201':
                print ("status is 201!")
                if isLoggedIn is not None:
                    print ('Please press confirm on your phone.')
                    isLoggedIn = None
            elif status != '408':
                break
        if isLoggedIn:
            print ("已经确认登陆了")
            break

    print ("==== here status is ", status)
    itchat.check_login()
    itchat.web_init()
    itchat.show_mobile_login()
    itchat.get_contact(True)
    # you can do your business here
    itchat.start_receiving()
    itchat.run()
