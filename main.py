from client.base.base import Base

class Test(Base):

    def __init__(self,config):
        """
        config[dict]
            -[x]hostname
            -[x]port
            -[x]username
            -[x]password
        """
        super().__init__(config)

# 测试代码
if __name__ == "__main__":
    config = {
        "hostname":"127.0.0.1",
        "port":"2222",
        "username":"vagrant",
        "password":"vagrant"
    }
    test_instance = Test(config=config)
    res = test_instance.ssh_client.execute_cmd("pwd")
    print(res)
