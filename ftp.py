#!/usr/local/bin/python3.8
# -*- coding=utf8 -*-
"""
# @Author : Eason Lee
# @Created Time : 2020/9/27 13:36
# @Description : 
"""
import ftplib


class FtpCls(object):
    def __init__(self, ftpserver, username, pwd, port=21):
        self.ftpserver = ftpserver
        self.username = username
        self.pwd = pwd
        self.port = port
        self.ftp = self.ftp_connect()

    # 建立 ftp 连接
    def ftp_connect(self):
        ftp = ftplib.FTP()
        try:
            ftp.connect(self.ftpserver, self.port)
            ftp.login(self.username, self.pwd)
        except:
            print('FTP login failed.')
        else:
            return ftp

    # 单个文件下载到本地
    def download_file(self, ftpfile, localfile):
        bufsize = 1024
        try:
            with open(localfile, 'wb') as fid:
                self.ftp.retrbinary('RETR {}'.format(ftpfile), fid.write, bufsize)
                self.ftp.close()
        except ftplib.error_perm:
            print("No such file or directory to download {}".format(ftpfile))
        else:
            return True

    # 上传单个文件
    def upload_file(self, ftpfile, localfile):
        bufsize = 1024
        try:
            with open(localfile, 'rb') as fid:
                self.ftp.storbinary('STOR {}'.format(ftpfile), fid, bufsize)
                self.ftp.close()
        except (OSError,FileNotFoundError):
            print("No such file or directory to upload {}".format(localfile))
        except:
            print("upload error")
        else:
            return True
