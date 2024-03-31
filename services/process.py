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
    def process_client(self):
        from client.process_client import Client as process_client
        return process_client(self.config)

    def get_all_process(self,sort_key):
        """
        查询全部进程，PID、CPU 使用率、内存使用率、完整命令行和命令名
        支持按cpu占用、内存占用排序
        """
        res = self.process_client.get_all_process(sort_key)
        process_arr = res.split("\n")[0:-1]
        process_all = []
        for process in process_arr:
            process = process.split()
            pid = process[0]
            cpu = process[1]
            mem = process[2]
            cmd = process[3]
            comm = process[4]
            process_dict = dict(pid=pid,cpu=cpu,mem=mem,cmd=cmd,comm=comm)
            process_all.append(process_dict)
        return process_all