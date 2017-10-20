# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "WeChatToken" # TODO: 从公众号的配置里获取

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return "hashcode != signature"
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print("Handle post web data is:", webData)
            recvMsg = receive.parse_xml(webData)

            if isinstance(recvMsg, receive.Msg) and recvMsg.MsgType == 'text':
                toUser = recvMsg.FromUserName
                fromUser = recvMsg.ToUserName
                content = recvMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                textMsg = replyMsg.send()
                print("Return to WeChat Msg is :", textMsg)
                return textMsg
            else:
                print("非文本信息，暂不处理")
                return 'success'
        except Exception, Argment:
            print("[ERROR]: except Exception!!!!:", Argment)
            return Argment














