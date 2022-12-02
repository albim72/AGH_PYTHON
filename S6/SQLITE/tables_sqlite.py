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

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"c:\sqlite\db\ptyhoncqlite.db"

    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects(
    id integer PRIMARY KEY,
    name text NOT NULL,
    begin_date text,
    end_date text
    );
    """
    
    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks(
    id integer PRIMARY KEY,
    name text NOT NULL,
    priority integer,
    status_id integer NOT NULL,
    project_id integer NOT NULL,
    begin_date text,
    end_date text,
    FOREIGN KEY (project_id) REFERENCES projects(id)
    );
    """
