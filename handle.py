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

            if isinstance(recvMsg, receive.Msg):
                toUser = recvMsg.FromUserName
                fromUser = recvMsg.ToUserName
                if recvMsg.MsgType == 'text':
                    replyMsg = reply.TextMsg(toUser, fromUser, recvMsg.Content)
                    textMsg = replyMsg.send()
                    print("Return to WeChat Msg is :", textMsg)
                    return textMsg
                if recvMsg.MsgType == 'image':
                    mediaId = recvMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    imageMsg = replyMsg.send()
                    return imageMsg
                else:
                    return reply.Msg().send()

            if isinstance(recvMsg, receive.EventMsg):
                if recvMsg.Event == 'CLICK':
                    if recvMsg.EventKey == 'mpGuide':
                        content = u'编写中，尚未完成'.encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            print("暂不处理......")
            return reply.Msg().send()
        except Exception, Argment:
            print("[ERROR]: except Exception!!!!:", Argment)
            return Argment














