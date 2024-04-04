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
    
    def find_file_by_name(self,addr,filename):
        """
        模糊查询，指定文件下的全部文件名
        """
        cmd = "find {} -name \"*{}*\" 2>/dev/null".format(addr,filename)
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res
    
    def show_file(self,addr):
        """
        显示文件
        """
        cmd = "cat {}".format(addr)
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res

    def find_file_word_count(self,word,addr):
        """
        查询指定文件中文本出现次数
        """
        cmd = "grep -o '{}' {} | wc -l".format(word,addr)
        res = self.ssh_client.execute_cmd(cmd)
        self.ssh_client.close_paramiko_client()
        return res