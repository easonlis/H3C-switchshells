# 功能菜单 
1. 导出交换机配置
2. 导入交换机配置
3. 绑定IP-MAC地址
4. 解除IP-MAC绑定
5. 导出所有 IP-MAC 绑定记录
6. 查找指定 MAC 或 IP 所在位置
7. 添加内网翻墙 IP(先绑定 IP-MAC)
8. 删除内网翻墙 IP(先解绑 IP-MAC)
9. 更改指定端口 VLAN
0. 退出程序 

# 说明

1. 该交换机脚本功能列表如上
2. main.py 是程序主入口
3. main.py 调用 ftp.py,实现功能【1】【2】
4. main.py 调用 HexinCaozuo.py,实现功能【3】【4】【5】【6】【7】【8】
5. main.py 调用 JiaohuanjiCaozuo.py,实现功能【6】【9】

operate_switches.py 可以对所有交换机进行统一操作，需要先定义好要操作的交换机列表、
操作指令，例如统一修改密码


# 用到的库
pip install netmiko