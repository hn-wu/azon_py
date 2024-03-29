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
    
    def get_ip_addr(self):
        """
        查询主机的全部网络配置：网口名、ip、掩码、mac地址、网络接口状态
        """
        cmd = "ip addr show"
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res
    
    def get_route(self):
        """
        查询静态路由
        """
        cmd = "ip route"
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res
    
    def get_netstat_port(self):
        """
        查询网络端口占用：协议、监听地址、状态、pid、进程名
        """
        cmd = "netstat -tulnp"
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res