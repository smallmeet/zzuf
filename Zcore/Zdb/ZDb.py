#encode:utf-8
import sys
sys.path.append('../')
import sqlite3

"""
This class is to handle the data storing more easily

"""
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

class ZDb:
    def __init__(self, db_name):
        self.db_name = db_name
        
        
@singleton
class ZDbManager:
    def __init__(self):
        
        """
        all_dbs : db_name by group
            for example:
                {'target_url':['url_info.db'],
                 'page_urls':['same_domain_urls.db', 'other_domain_urls']
                 'server':[server_port.db, 'server_info.db']
                 ...
                 }
        """
        self.all_dbs = dict()
        
        """curser_tables : get_every db' s conn or curser"""
        self.conn_tables = dict()
    
    def get_dbs(self, group = "", db_names = []):
        """
        Input db_names in a list
            if you put a other(except a list) as db_names in this
            method , it will return 0 as a error
        """
        if not isinstance(db_names, list):
            raise TypeError("Excepted Object of type list, get {}".
                            format(type(db_names).__name__))
        
        if not isinstance(group, str):
            raise TypeError("Excepted Object of type str , get {}".
                            format(type(group).__name__))
        
        """Store database info"""
        if self.all_dbs.has_key(group) == True:
            """There some problems here! Attention!"""
            self.all_dbs[group] = self.all_dbs[group] + db_names
        else:
            self.all_dbs[group] = db_names
            
        
    
        