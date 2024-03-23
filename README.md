# azon_py
提供api以ssh的方式管理多主机
实现功能
1. ssh登录后台执行命令
2. ssh登录后台，进入容器内执行命令【自定义如何进入容器】
3. 搜集文件，并打包【文件位置模板模板】
4. 全局搜索文件
5. 配置网络【ip、掩码、网关】
6. 查询网络配置【网口名、ip、静态路由、dns】
7. 批量执行，允许将用户设为一个组

项目架构：
    前端：Vue
    后端：python
    内嵌数据库：TinyDB

分层

一、client层
base层
    db_client.py[crud TinyDB]
    ssh_cmd_client.py[ssh执行命令]
network_client.py[执行网络命令]
file_client.py[执行文件相关命令]
user_config_client.py[记录用户配置]

二、services层
ssh_cmd_api.py[直接执行命令，数据处理]
network_api.py[执行网络相关命令，数据处理]
file_api.py[执行文件相关命令，数据处理]
user_config_api.py[记录用户配置，数据处理]

三、api层
ssh_cmd_api.py[直接执行命令的api]
network_api.py[执行网络相关命令的api]
file_api.py[执行文件相关命令的api]
user_config_api.py[记录用户配置的api]
