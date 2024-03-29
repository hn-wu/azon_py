from services.base.base import Base as BaseService
from functools import cached_property
import re

class Service(BaseService):

    def __init__(self,config):
        """
        config[dict]
            -[x]hostname
            -[x]port
            -[x]username
            -[x]password
            -[]dbname
        """
        super().__init__(config)
    
    @cached_property
    def network_client(self):
        from client.network_client import Client as network_client
        return network_client(self.config)

    def get_ip_addr(self):
        """
        查询主机的全部网络配置：网口名、ip、掩码、mac地址、网络接口状态
        """
        res = self.network_client.get_ip_addr()
        interfaces = {}
        interface_blocks = re.findall(r'\d+: [^\n]+(?:\n\s+[^\n]+)+', res)
        for block in interface_blocks:
            # 获取接口名称
            interface_name = re.search(r'\d+: (\S+):', block).group(1)
            # 获取网络接口状态
            interface_state = re.search(r'<([^>]+)>', block).group(1).split(",")                
            # 获取ip和掩码
            interface_ip = re.search(r'inet (\d+\.\d+\.\d+\.\d+/\d+)', block).group(1)
            # 获取mac地址
            interface_mac = re.search(r'link/\S+ (?P<mac>(?:[0-9a-f]{2}:){5}[0-9a-f]{2}).*?', block).group(1)
            # 将接口信息存储到字典中
            interfaces[interface_name] = dict(interface_name=interface_name,interface_state=interface_state,
                                              interface_ip=interface_ip,interface_mac=interface_mac)
        return interfaces
    
    def get_route(self):
        """
        查询静态路由
        """
        res = self.network_client.get_route().split("\n")
        route_arr = []  
        for route in res[:-1]:
            default = False
            first = route.split(' ', 1)[0]
            dev = re.search(r'dev (\S+)', route).group(1)
            src = re.search(r'src (\d+\.\d+\.\d+\.\d+)', route).group(1)
            ip = first
            if route.startswith("default"):
                default = True
                ip = re.search(r'via (\d+\.\d+\.\d+\.\d+)', route).group(1)
            route_dict = dict(default=default,ip=ip,dev=dev,src=src)
            route_arr.append(route_dict)
        return route_arr
    
    def get_netstat_port(self):
        """
        查询网络端口占用：协议、监听地址、状态、pid、进程名
        """
        res = self.network_client.get_netstat_port().split("\n")
        netstat_arr = []
        for netsta in res[2:-1]:
            netsta = netsta.split()
            proto = netsta[0]
            if "tcp" in proto:
                proto = netsta[0]
                LocalAddress = netsta[3]
                state = netsta[5]
                process = netsta[6]
                netstat_dict = dict(proto=proto,LocalAddress=LocalAddress,state=state,process=process)
                netstat_arr.append(netstat_dict)
        return netstat_arr