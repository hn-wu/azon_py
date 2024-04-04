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
    def file_client(self):
        from client.file_client import Client as file_client
        return file_client(self.config)
    
    def find_file_by_name(self,addr,filename):
        """
        模糊查询，指定文件下的全部文件名
        """
        res = self.file_client.find_file_by_name(addr,filename)
        file_name = res.split("\n")
        return file_name[0:-1]
    
    def show_file(self,addr):
        """
        显示文件
        """
        res = self.file_client.show_file(addr)
        return res
    
    def find_file_word_count(self,word,addr):
        """
        查询指定文件中文本出现次数
        """
        res = self.file_client.find_file_word_count(word,addr)
        count = res.split("\n")[0:-1][0]
        file_count_word = dict(word=word,count=count,addr=addr)
        return file_count_word