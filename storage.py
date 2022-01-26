import logging
from distutils.log import Log
from mysql.connector import connect, Error
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
                self.cursor.execute("SELECT value FROM task_meta WHERE name = \"Version\"")
                data = self.cursor.fetchall()
                if len(data) == 0:
                    self.__initDB()
                    return
            except Error:
                self.__initDB()
                return
        except Exception as e:
            raise e

    def __initDB(self):
        logging.info("Initializing database")
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS task_meta(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(60) NOT NULL, value VARCHAR(60), UNIQUE(name))")
            self.cursor.execute("INSERT INTO task_meta (name, value) VALUES (\"VERSION\",%s)", ((self.ver.public)))
            self.db.commit()
        except Exception as e:
            raise e