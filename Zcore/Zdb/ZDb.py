#encode:utf-8
import sys
sys.path.append('../')
import sqlite3
import errno

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
    def __init__(self, group = "", db_name=""):
        self.db_name = db_name
        
        self.conn = None
        self.cursor = None
        
        self.__create_db()

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
        
        self.conn = sqlite3.connect('Zzuf.db')
        self.__init_tables()
        self.cursor = conn.cursor()
    
    def __init_tables():
        try:
            """TBD"""
            pass
        except sqlite3.Error e:
            print errno(e)
    
    def has_table(self, table_name = ""):
        self.cursor.execute('select name form sqlite_master ')
        for table in self.cursor.fetchall():
            if table_name in table:
                return True
        return False
    
    def execute(self, query):
        try:
            self.cursor.execute(query)
        except sqlite3.Error e:
            print "[!]DB ERROR!"
            
    def commit(self):
        try:
            self.conn.commit()
        except sqlite3.Error e:
            print "[!]DB ERROR!"
    def close(self):
        """Close DB"""
        self.cursor.close()
        self.conn.close()
            
    
    
        
    
if __name__ == '__main__':
    
    """proof singleton"""
    a = ZDbManager()
    b = ZDbManager()
    
    a.all_dbs['s'] = 1
    b.all_dbs['b'] = 3
    
    print a.all_dbs