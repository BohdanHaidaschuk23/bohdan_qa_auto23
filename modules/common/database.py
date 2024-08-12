import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(r'C://Users//haida//Desktop//local_repo//bohdan_qa_auto23' + r'become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connection successfull. Data version is : {record}")