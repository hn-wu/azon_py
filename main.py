from client.base.base import Base
from tinydb import TinyDB, Query

class Test(Base):

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

def __build_query__(query_conditions):
        Q = Query()
        query = None
        for field, value in query_conditions.items():
            condition = (Q[field] == value)
            if query is None:
                query = condition
            else:
                query &= condition
        return query

# 测试代码
if __name__ == "__main__":
    config = {
        "hostname":"127.0.0.1",
        "port":"2222",
        "username":"vagrant",
        "password":"vagrant",
        "dbname":"test"
    }
    test_instance = Test(config=config)
    record = {'type': 'apple', 'count': 7}
    query_conditions = {'type': 'apple'}
    res = test_instance.db_client.search_eq_db(query_conditions)
    print(res)
