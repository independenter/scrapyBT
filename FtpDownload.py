#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

from ftplib import FTP
#
class DownloadFtp(object):
    host = "yg72.dydytt.net"
    port=8181
    username = 'ygdy8'
    pwd = 'ygdy8'
    def __init__(self):
        print("初始化FTP下载工具")

    def getContext(self,ftp_url):
        print("即将下载ftp：%s" % ftp_url)
        ftp = FTP('ftp.debian.org')
        ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        ftp.login()
        '''
        cwd(path) 把当前工作目录设置为 path 所示的路径
        dir ([path[,...[,cb]]) 显示 path 目录里的内容，可选的参数 cb 是一个回调函数，会传递给 retrlines()方法
        nlst ([path[,...]) 与 dir()类似， 但返回一个文件名列表，而不是显示这些文件名
        retrlines(cmd [, cb]) 给定 FTP命令（如“ RETR filename”），用于下载文本文件。可选的回调函数 cb 用于处理文件的每一行
        retrbinary(cmd,cb[,bs=8192[, ra]]) 与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块（块大小默认为 8KB）下载的数据
        storlines(cmd, f) 给定 FTP 命令（如“ STOR filename”），用来上传文本文件。要给定一个文件对象 f
        storbinary(cmd, f,[,bs=8192]) 与 storlines()类似，只是这个指令处理二进制文件。要给定一个文件对象 f，上传块大小 bs 默认为 8KB
        rename(old, new) 把远程文件 old 重命名为 new
        delete(path) 删除位于 path 的远程文件
        mkd(directory) 创建远程目录
        rmd(directory) 删除远程目录
        quit() 关闭连接并退出
        '''
        ftp.cwd('debian')
        print(ftp.retrlines('LIST'))
        ftp.retrbinary('RETR README', open('README', 'wb').write)
        ftp.quit()


class DownloadMagnet(object):
    def __init__(self):
        print("初始化此例连接下载工具下载工具")

    def getContext(self,magnet_link):
        print("即将下载ftp：%s" % magnet_link)

if __name__=='__main__':
    # ftp_url='ftp://ygdy8:ygdy8@yg72.dydytt.net:8181/阳光电影www.ygdy8.com.茉莉牌局.BD.720p.中英双字幕.mkv'
    # down = DownloadFtp()
    # down.getContext(ftp_url)
    magnet_link='magnet:?xt=urn:btih:4e9a0c36c1f6d971a034b8f86aa950efecd1605e&dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1www.ygdy8.com.X%e6%88%98%e8%ad%a6%ef%bc%9a%e5%a4%a9%e5%90%af.BD.720p.%e5%9b%bd%e8%8b%b1%e5%8f%8c%e8%af%ad%e5%8f%8c%e5%ad%97.mkv&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=udp%3a%2f%2feddie4.nl%3a6969%2fannounce&tr=udp%3a%2f%2fshadowshq.eddie4.nl%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce'
    down = DownloadMagnet()
    down.getContext(magnet_link)