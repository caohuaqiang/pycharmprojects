import mysql.connector


class UseDataBase:
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor(buffered=True)
            return self.cursor
        except Exception as err:
            print(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
