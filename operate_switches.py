#!/usr/local/bin/python3.8
# -*- coding=utf8 -*-
"""
# @Author : Eason Lee
# @Created Time : 2020/9/28 13:53
# @Description : 
"""
from netmiko import ConnectHandler

# 交换机登录账号密码
switch_adm, switch_passd = 'admin', 'MYDM@12#$'
# 要操作的交换机列表，请按需要更改
operate_switches = [
    '192.168.*.*', '192.168.*.*', '192.168.*.*',
    '192.168.*.*', '192.168.*.*', '192.168.*.*',
]
# 在交换机上要操作的一系列指令，请按需要更改
operate_commands = [
    'no archive configuration server',
    'save force'
]


# 连接交换机
def connect(ip, username, password, port=22, device_type="huawei"):
    login_info = {
        # 如果需要一次显示多行如 dis curr ，切换为 hp_comware 才可以
        # 'device_type': 'hp_comware'
        'ip': ip,
        'username': username,
        'password': password,
        'port': port,
        'device_type': device_type,
    }
    net_connect = ConnectHandler(**login_info)
    # sshConfirm = net_connect.find_prompt()
    # print('login' + sshConfirm)
    return net_connect


# 对交换机进行操作
def operates(switches, commands):
    for switch in switches:
        net_connect = connect(switch, switch_adm, switch_passd)
        sshConfirm = net_connect.find_prompt()
        print('login ' + sshConfirm)
        output = net_connect.send_config_set(commands)
        print(output)
        net_connect.disconnect()
        #


operates(operate_switches, operate_commands)
