import logging
from distutils.log import Log
from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from packaging import version

class DatabaseStorage:
    def __init__(self, dbhost, dbname, dbuser, dbpass):
        self.ver = version.parse("0.0.1")
        self.db = connect(host=dbhost,user=dbuser,password=dbpass,database=dbname)
        self.cursor = self.db.cursor()
        self.__checkDBInit()

    def __checkDBInit(self):
        try:
            try:
                resp = self.cursor.execute("SELECT value FROM task_meta WHERE name = \"Version\"")
                data = resp.fetchall()
                if len(data) == 0:
                    self.__initDB()
            except mysql.connector.Error:
                self.__initDB()
        except Exception as e:
            raise e

    def __initDB(self):
        logging.info("Initializing database")
        try:
            self.cursor.execute("CREATE TABLE task_meta id INT AUTO_INCREMENT PRIMARY KEY, name UNIQUE VARCHAR(60) NOT NULL, value VARCHAR(60)")
            self.cursor.execute("INSERT INTO task_meta (name, value) VALUES (\"VERSION\",%s)", (self.ver.Version()))
            self.db.commit()
        except Exception as e:
            raise e