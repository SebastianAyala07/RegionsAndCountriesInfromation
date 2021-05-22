import sqlite3
from sqlite3.dbapi2 import connect

STR_CREATE = """
    CREATE TABLE IF NOT EXISTS INFOREGIONS(
        region varchar(64),
        city_name varchar(64),
        language varchar(64),
        time float
    )
"""


class Connection():

    @classmethod
    def create_db(cls):
        connection = cls.get_conn()
        cursor = connection.cursor()
        cursor.execute(STR_CREATE)
        cursor.commit()
        connection.close()

    @classmethod
    def get_conn(self):
        return sqlite3.connect('INFOREGIONS.db')


class InteractionsDatabase():

    def save_
