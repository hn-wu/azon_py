from functools import cached_property
import logging
from tinydb import TinyDB, Query


class Client:

    def __init__(self,config):
        """
        config[dict]
            -[x]dbname
        """
        self.config = config
    
    @cached_property
    def db_client(self):
        """
        创建或打开名为db.json的文件作为数据库
        """
        if self.config["dbname"] is None:
            return None
        dbname=self.config["dbname"]
        dbname = "{}.json".format(dbname)
        db_client = TinyDB(dbname)
        return db_client

    def insert_db(self,record):
        """
        插入db
            -[x]record[dict]
        """
        self.db_client.insert(record)

    def insert_multiple_db(self,record_arr):
        """
        批量插入db
            -[x]record_arr[arr]
                -[]record[dict]
        """
        self.db_client.insert(record_arr)
    
    def search_eq_db(self,query_conditions):
        """
        根据条件等值查询db
            -[x]query_conditions[dict]
        """
        query = self.__build_query__(query_conditions)
        results = self.db_client.search(query)
        return results
    
    def update_eq_db(self,record,query_conditions):
        """
        根据条件等值更新db
            -[x]record[dict]
            -[x]query_conditions[dict]
        """
        query = self.__build_query__(query_conditions)
        self.db_client.update(record, query)
    
    def delete_eq_db(self,query_conditions):
        """
        根据条件等值删除db
            -[x]query_conditions[dict]
        """
        query = self.__build_query__(query_conditions)
        self.db_client.remove(query)

    def __build_query__(self,query_conditions):
            Q = Query()
            query = None
            for field, value in query_conditions.items():
                condition = (Q[field] == value)
                if query is None:
                    query = condition
                else:
                    query &= condition
            return query
    
    def close_db(self):
        self.db_client.close()