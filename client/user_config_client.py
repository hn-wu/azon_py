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
    
    def set_ssh_config(self):
        record = self.config.copy()
        record.pop("dbname") 
        self.db_client.insert_db(record)
        self.db_client.close_db()

    def get_ssh_config_by_hostname(self):
        hostname = self.config.get("hostname")
        query_conditions = dict(hostname=hostname)
        ssh_config = self.db_client.search_eq_db(query_conditions)
        self.db_client.close_db()
        return ssh_config
    
    def get_ssh_config_all(self):
        ssh_config = self.db_client.search_all()
        self.db_client.close_db()
        return ssh_config