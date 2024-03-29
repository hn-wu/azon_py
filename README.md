# azon_py
提供api以ssh的方式管理多主机
实现功能
一、命令行
1. 主机内查询
2. 容器内查询
3. 循环执行命令
for i in {1..次数}; do 命令; sleep 秒数; done
for i in {1..5}; do echo $i; sleep 1; done

二、网络
1. 查询主机的全部网络配置：网口名、ip、掩码、mac地址、网络接口状态
ip addr show
2. 查询静态路由
ip route
3. 查询网络端口占用：协议、监听地址、状态、pid、进程名
netstat -tulnp

三、文件
1. 模糊查询，指定文件下的全部文件名
find /地址名 -name "*.txt" 2>/dev/null
2. 查询指定文件中文本出现次数
grep -o '查询单词' /文件名 | wc -l
3. 将文件打包，并下载

四、进程
1. 查询全部进程，pid、cpu占用、内存占用、启动cmd【ps -eo pid,%cpu,%mem,cmd,comm --no-headers】【支持按cpu占用、内存占用排序】
ps -eo pid,%cpu,%mem,cmd,comm --no-headers --sort=-pid
ps -eo pid,%cpu,%mem,cmd,comm --no-headers --sort=-%cpu
ps -eo pid,%cpu,%mem,cmd,comm --no-headers --sort=-%mem


五、用户相关
1. 存储ssh主机配置
2. ssh主机分组

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
process_client.py[进程配置]

二、services层
ssh_cmd.py[直接执行命令，数据处理]
network.py[执行网络相关命令，数据处理]
file.py[执行文件相关命令，数据处理]
user_config.py[记录用户配置，数据处理]
process.py[进程配置]

三、api层
ssh_cmd_api.py[直接执行命令的api]
network_api.py[执行网络相关命令的api]
file_api.py[执行文件相关命令的api]
user_config_api.py[记录用户配置的api]
process_api.py[进程配置api]
