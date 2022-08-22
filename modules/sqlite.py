import time
import sqlite3

class SQLite():

    def __init__(self) -> None:
        db = sqlite3.connect("users.sqlite")
        sql_request = db.cursor()
        sql_request.execute("""CREATE  TABLE IF NOT EXISTS users_requests(
                            user TEXT,
                            date_request TEXT
                        )""")
        db.commit()

    def write_DATA_SQLITE(self, dict_data):
        date = time.strftime(": %H:%M:%S - %d.%m.%y")
        db = sqlite3.connect("users.sqlite")
        sql_request = db.cursor()
        sql_request.execute(f"INSERT INTO users_requests VALUES(?, ?)", (dict_data["name"][0], date))
        db.commit()
        sql_request.execute("SELECT * FROM users_requests")
        sql_request.close

    def read_DATA_SQLITE(self):
        db = sqlite3.connect("users.sqlite")
        sql_request = db.cursor()
        sql_request.execute("SELECT * FROM users_requests")
        sel_req  = sql_request.fetchall()
        sql_request.close
        return sel_req

    def fetch_DATA_SQLITE(self, user):
        db = sqlite3.connect("users.sqlite")
        sql_request = db.cursor()
        sql_request.execute('SELECT * FROM users_requests WHERE user = "{}"'.format(user))
        user_data  = sql_request.fetchall()
        sql_request.close
        return user_data
