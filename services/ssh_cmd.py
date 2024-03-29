from services.base.base import Base as BaseService

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
    
    def execute_cmd(self,cmd):
        """
        ssh执行命令
        """
        res = self.ssh_client.execute_cmd(cmd=cmd)
        self.ssh_client.close_paramiko_client()
        return res
    
    def execute_cmd_while(self,count,cmd):
        """
        循环ssh执行命令
        """
        res = self.ssh_client.execute_cmd_while(count=count,cmd=cmd)
        self.ssh_client.close_paramiko_client()
        return res

    def execute_cmd_container(self,cmd,container_id):
        """
        在容器内执行命令
        """
        res = self.ssh_client.execute_cmd_container(cmd=cmd,container_id=container_id)
        self.ssh_client.close_paramiko_client()
        return res