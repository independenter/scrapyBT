#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import socket,threading

appid = 1400079418
appkey = "5352da4430a836e72e111b3128e2c57b"
phone_number = "15501951002" #手机号可以添加多个多个
template_id = 102177

ssender = SmsSingleSender(appid, appkey)
params = ["321456","5"]  #发送验证码为1234
# try:
#     result = ssender.send_with_param(86, phone_number,
#         template_id, params)
# except HTTPError as e:
#     print(e)
# except Exception as e:
#     print(e)

# print(result)

class websocket_server(threading.Thread):
    def __init__(self, port):
        super(websocket_server, self).__init__()
        self.port = port

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        sock.bind((host, self.port))
        sock.listen(5)
        print('websocket server started!',self.port)
        while True:
            client, addr = ser.accept()
            print("accept %s connect" % (addr,))
            data = client.recv(1024)
            # print(host,addr,client)
            if data:
                sendMsg = host + " say:" + data.decode('utf-8')
                # sendMsg = addr[host] + " say:" + data
                client.send(sendMsg.encode('utf-8'))
            # print(data.decode('utf-8'))
            # client.send('get'.encode('utf-8'))
            client.close()

if __name__=='__main__':
    server = websocket_server(9000)
    server.run()
