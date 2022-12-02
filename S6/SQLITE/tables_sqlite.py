import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as a:
        print(a)
    return conn

def create_project(conn,project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?)
    """
    
    cur = conn.cursor()
    cur.execute(sql,project)
    conn.commit()
    return cur.lastrowid


def create_task(conn,task):
    sql = """
    INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?)
    """

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid
