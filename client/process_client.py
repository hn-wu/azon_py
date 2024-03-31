from client.base.base import Base as BaseClient

class Client(BaseClient):

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

    def get_all_process(self,sort_key="pid"):
        """
        查询全部进程，PID、CPU 使用率、内存使用率、完整命令行和命令名
        支持按cpu占用、内存占用排序
        """
        cmd = ""
        base_cmd = "ps -eo pid,%cpu,%mem,cmd,comm --no-headers "
        if sort_key in "pid":
            cmd = base_cmd + "--sort=-pid"
        elif sort_key in "cpu":
            cmd = base_cmd + "--sort=-%cpu"
        elif sort_key in "mem":
            cmd = base_cmd + "--sort=-%mem"
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res