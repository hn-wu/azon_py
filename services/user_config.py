from services.base.base import Base as BaseService
from functools import cached_property

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
    def user_config_client(self):
        from client.user_config_client import Client as user_config_client
        return user_config_client(self.config)
    
    def set_ssh_config(self):
        self.user_config_client.set_ssh_config()

    def get_ssh_config_by_hostname(self):
        ssh_config = self.user_config_client.get_ssh_config_by_hostname()
        return ssh_config
    
    def get_ssh_config_all(self):
        ssh_config_arr = self.user_config_client.get_ssh_config_all()
        return ssh_config_arr