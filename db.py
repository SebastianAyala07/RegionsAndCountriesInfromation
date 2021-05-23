import sqlite3

STR_CREATE = """
    CREATE TABLE IF NOT EXISTS INFOREGIONS(
        region varchar(64),
        city_name varchar(64),
        language varchar(64),
        time float
    )
"""

STR_INSERT = """
    INSERT INTO INFOREGIONS(region, city_name, language, time) VALUES ({});
"""


class Connection():

    @classmethod
    def create_db(cls):
        connection = cls.get_conn()
        cursor = connection.cursor()
        cursor.execute(STR_CREATE)
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def get_conn(cls):
        return sqlite3.connect('INFOREGIONS.db')


class InteractionsDatabase():

    @classmethod
    def save_info_regions(cls, dataframe):
        connection = Connection.get_conn()
        cursor = connection.cursor()
        try:
            for series in dataframe.iloc:
                str_supplementary = ""
                for record in series:
                    if f'{type(record)}' == "<class 'numpy.float64'>":
                        str_supplementary += f'{record}'
                    else:
                        str_supplementary += f"\'{record}\',"
                cursor.execute(STR_INSERT.format(str_supplementary))
            connection.commit()
        except:
            print("An error has occurred at the database level")
            connection.rollback()
