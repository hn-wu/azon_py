from functools import cached_property

class Base:

    def __init__(self,config):
        """
        config[dict]
            -[x]hostname
            -[x]port
            -[x]username
            -[x]password
            -[]dbname
        """
        self.config = config
    
    @cached_property
    def ssh_client(self):
        from client.base.ssh_cmd_client import Client as ssh_cmd_client
        return ssh_cmd_client(self.config)
    
    @cached_property
    def db_client(self):
        from client.base.db_client import Client as db_client
        return db_client(self.config)