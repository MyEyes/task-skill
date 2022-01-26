import logging

class Schema_v_0_0_1():
    def __init__(self):
        pass

    def create_schema(self, db):
        logging.info("Initializing database")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_meta(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(60) NOT NULL,
            value VARCHAR(60),
            UNIQUE(name))""")
        
        #Table containing task categories
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_category(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(60) NOT NULL,
            created DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(name))""")

        #Table containing task definitions
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_taskDef(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(60) NOT NULL,
            active INT DEFAULT 0,
            created DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(name))""")

        #Table containing spoken phrases
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_taskPhrase(
            id INT AUTO_INCREMENT PRIMARY KEY,
            phrase VARCHAR(128) NOT NULL,
            created DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(phrase))""")
        
        #Relationship linking phrases to tasks
        cursor.execute("""CREATE TABLE IF NOT EXISTS task_taskPhrase2Def(
            def_id INT NOT NULL,
            phrase_id INT NOT NULL,
            INDEX(def_id),
            FOREIGN KEY(def_id) REFERENCES task_taskDef(id),
            INDEX(phrase_id),
            FOREIGN KEY(phrase_id) REFERENCES task_taskPhrase(id)
            )""")

    def set_data(self, db):
        cursor = db.cursor()
        data = ("Version", "0.0.1")
        cursor.execute("INSERT INTO task_meta (name, value) VALUES (%s,%s)", data)
