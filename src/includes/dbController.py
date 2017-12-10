import MySQLdb as db
from settings import dbConfig

class DbController :
    def __init__(self, cfg = dbConfig()):
        self.host = cfg['host']
        self.user = cfg['user']
        self.passwd = cfg['passwd']
        self.db = cfg['db']
        self.connection = db.connect(self.host, self.user, self.passwd, self.db);
        self.rowcount = -1
        self.lastInsertedId = -1

    
    def __del__(self):
        if self.connection :
            self.connection.close()

    def execute(self, query, data = None):
        self.rowcount = -1
        self.lastrowid = -1
        try:
            if self.connection :
                cursor = self.connection.cursor()
                cursor.execute(query, data)
                self.rowcount =  cursor.rowcount
                self.lastInsertedId = self.connection.insert_id()
                self.connection.commit()
        except Exception as e:
            raise e

    def executeSelect(self, query, data = None):
        try:
            if self.connection :
                cursor = self.connection.cursor(db.cursors.DictCursor)
                cursor.execute(query, data)
                return cursor.fetchall()
        except Exception as e:
            raise e
