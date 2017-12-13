import pymysql as db
from settings import db_config


class DbController:
    def __init__(self, cfg=db_config()):
        self.host = cfg['host']
        self.user = cfg['user']
        self.password = cfg['password']
        self.db = cfg['db']
        self.connection = db.connect(
            self.host,
            self.user,
            self.password,
            self.db
            )
        self.row_count = -1
        self.last_inserted_id = -1
        self.last_row_id = -1

    def __del__(self):
        if self.connection:
            self.connection.close()

    def execute(self, query, data=None):
        self.row_count = -1
        self.last_row_id = -1
        try:
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query, data)
                self.row_count = cursor.rowcount
                self.last_inserted_id = self.connection.insert_id()
                self.connection.commit()
        except Exception as e:
            raise e

    def execute_select(self, query, data=None):
        try:
            if self.connection:
                cursor = self.connection.cursor(db.cursors.DictCursor)
                cursor.execute(query, data)
                self.row_count = cursor.rowcount
                return cursor.fetchall()
        except Exception as e:
            raise e
