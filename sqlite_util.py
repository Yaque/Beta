import sqlite3
import time


def create_database_word_data(word_database_name):
    conn = sqlite3.connect("word_database/" + word_database_name +".db")
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS WORD
           (ID INT PRIMARY KEY     NOT NULL,
           START_TIME           TEXT    NOT NULL,
           END_TIME            TEXT     NOT NULL,
           WORD        TEXT   NOT NULL);''')
    # print("Table created successfully")
    conn.close()

def insert_word_data(word_database_name, id, start_time, end_time, word):
    create_database_word_data(word_database_name)
    conn = sqlite3.connect("word_database/" + word_database_name +".db")
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute("INSERT INTO WORD (ID,START_TIME,END_TIME,WORD) VALUES ("+ id + ", '" + start_time  + "', '" + end_time + "', '" + word + "' )")
    conn.commit()
    conn.close()

def create_database():
    conn = sqlite3.connect("beta.db")
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS BETA
           (ID INT PRIMARY KEY     NOT NULL,
           APP_ID           TEXT    NOT NULL,
           API_KEY            TEXT     NOT NULL,
           SECRET_KEY        TEXT   NOT NULL);''')
    # print("Table created successfully")
    conn.close()

def insert():
    create_database()
    conn = sqlite3.connect("beta.db")
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute("INSERT INTO BETA (ID,APP_ID,API_KEY,SECRET_KEY) \
          VALUES (1, '10883007', 'oT0maOpZnyFINOqheksRLur0', 'W4pSDA4W1ltIYZp6fPaIb5HssSbhTGCB' )")
    conn.commit()
    conn.close()

def query():
    create_database()
    conn = sqlite3.connect("beta.db")
    # print("Opened database successfully")
    c = conn.cursor()
    cursor = c.execute("SELECT ID, APP_ID, API_KEY, SECRET_KEY  FROM BETA")
    bate = []
    for row in cursor:
        # print("ID = ", row[0])
        # print("NAME = ", row[1])
        # print("ADDRESS = ", row[2])
        # print("SALARY = ", row[3], "\n")
        bate.append(row[0])
        bate.append(row[1])
        bate.append(row[2])
        bate.append(row[3])
    conn.close()
    # print(bate)
    return bate

def update(app_id, api_key, secret_key):
    try:
        insert()
    except:
        pass
    conn = sqlite3.connect("beta.db")
    c = conn.cursor()
    c.execute("UPDATE BETA SET APP_ID = '" + app_id + "' where ID=1")
    c.execute("UPDATE BETA SET API_KEY = '" + api_key + "' where ID=1")
    c.execute("UPDATE BETA SET SECRET_KEY = '" + secret_key + "' where ID=1")
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("beta.db")
    c = conn.cursor()
    c.execute("DELETE FROM BETA WHERE ID = 1")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # create_database()
    # insert()
    # query()
    # update("1", "2", "3")
    # query()
    # delete()
    pass
