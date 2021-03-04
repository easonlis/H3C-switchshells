#!/usr/local/bin/python3.8
# -*- coding=utf8 -*-
"""
# @Author : Eason Lee
# @Created Time : 2020/9/24 17:56
# @Description : 
"""
import re,time,random,logging
import ftp,os
from HexinCaozuo import HexinCaozuo
from JiaohuanjiCaozuo import JiaohuanjiCaozuo
logging.basicConfig(filename="test.log", level=logging.DEBUG)

menu = ("""
========== 功能菜单 ==========
【1】 导出交换机配置
【2】 导入交换机配置
【3】 绑定IP-MAC地址
【4】 解除IP-MAC绑定
【5】 导出所有 IP-MAC 绑定记录
【6】 查找指定 MAC 或 IP 所在位置
【7】 添加内网翻墙 IP(先绑定 IP-MAC)
【8】 删除内网翻墙 IP(先解绑 IP-MAC)
【9】 更改指定端口 VLAN
【10】 导出翻墙 IP 记录
【0】 退出程序 
========== 功能菜单 ==========
""")

# 交换机列表
switches = [
    '192.168.*.*', '192.168.*.*', '192.168.*.*',
    '192.168.*.*', '192.168.*.*', '192.168.*.*',
]

# 核心上各聚合端口对应连接的交换机
bagges = {
    'BAGG1': '192.168.*.*', 'BAGG2': '192.168.*.*', 'BAGG3': '192.168.*.*',
    'BAGG4': '192.168.*.*', 'BAGG5': '192.168.*.*', 'BAGG6': '192.168.*.*',
}

# 交换机登录账户，ftp登录账户
adm, adm_pwd ='admin', 'admin123'
ftp_usr, ftp_pwd ='ftp', 'ftp123'


def get_controller(index):
    # 1.导出所有交换机配置
    if index == '1':
        ftpfile = "startup.cfg"
        if not os.path.exists("../switch-config/"):
            os.mkdir("../switch-config/")
        save_path = "../switch-config/{}-{}.cfg"
        for host in switches:
            session = ftp.FtpCls(host, ftp_usr, ftp_pwd)
            localfile = save_path.format(host, time.strftime("%Y%m%d"))
            result = f"{host} 备份成功" if session.download_file(ftpfile, localfile) else f"{host} 备份失败"
            print(result)

    # 2.上传文件到指定交换机
    elif index == '2':
        host = ''
        while host not in switches:
            host = input("上传到哪台交换机(IP格式): ")
        localfile = input("请输入上传文件的绝对路径: ")
        ftpfile = input("在交换机另存为(文件名): ")
        print("正在上传 {} 到 {} 为 {} ......".format(localfile, host, ftpfile))
        session = ftp.FtpCls(host, ftp_usr, ftp_pwd)
        result = "上传成功" if session.upload_file(ftpfile, localfile) else "上传失败"
        print(result)

    # 3.绑定 IP-MAC 地址
    elif index == '3':
        core.bangding_ipmac()

    # 4.解除 IP-MAC 绑定
    elif index == '4':
        core.jiechu_ipmac()

    # 5.导出所有 IP-MAC 绑定记录
    elif index == '5':
        core.daochu_ipmac()

    # 6.查找指定 MAC 或 IP 所在位置
    elif index == '6':
        mac, bagg = core.cha_weizhi()
        if mac is not None and bagg is not None:
            switch = JiaohuanjiCaozuo(bagges.get(bagg), adm, adm_pwd)
            switch.locate(mac)
        else:
            pass

    # 7.添加内网翻墙 IP(先绑定 IP-MAC)
    elif index == '7':
        core.jia_fanq()

    # 8.删除内网翻墙 IP(先解绑 IP-MAC)
    elif index == '8':
        core.shan_fanq()

    # 9.更改指定端口 VLAN
    elif index == '9':
       host = input("要操作的交换机IP:")
       if host in switches:
           switch = JiaohuanjiCaozuo(host, adm, adm_pwd)
           switch.operate()
       else:
           print("没有该交换机")

    elif index == '10':
        core.daochu_fanq()

    # 0.退出程序并进行保存
    elif index == '0':
        core.net_connect.send_command('save force')
        core.net_connect.disconnect()
        exit(1)


def random_print():
    zidian= {
        0: "哥~咱别搞错了行吗",
        1: "信不信给你个宝贝看看？嗯？",
        2: "哈哈，没想到吧这是错误选择",
        3: "好吧，你又按错了",
        4: "从前有只小毛驴，然后......它死了",
        5: "你猜猜接下来60秒会发生什么?......没错，一分钟就过去了"
    }
    print(zidian.get(random.randint(0, 5)))


if __name__ == '__main__':
    core = HexinCaozuo(adm, adm_pwd)
    while True:
        print(menu)
        try:
            controller = input("请输入功能编号：")
            if re.match(r'^[0-9]$|^10$', controller):
                get_controller(controller)
            else:
                random_print()
        except EOFError:
            core.net_connect.disconnect()
            exit(1)
