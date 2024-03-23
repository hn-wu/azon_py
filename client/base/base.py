from functools import cached_property

class Base:

    def __init__(self,config):
        """
        config[dict]
            -[x]hostname
            -[x]port
            -[x]username
            -[x]password
        """
        self.config = config
    
    @cached_property
    def ssh_client(self):
        from client.base.ssh_cmd_client import Client as ssh_cmd_client
        return ssh_cmd_client(self.config)