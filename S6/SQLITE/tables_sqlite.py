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

def main():
    database = r"c:\sqlite\db\ptyhoncqlite.db"

    conn = create_connection(database)

    with conn:
        project = ('Super Apka napisana w Pythonie','2021-02-02','2022-10-12')
        project_id = create_project(conn,project)
        task_1 = ('Analiza wymagań dotyczących aplikacji',1,1,project_id,'2021-02-08','2021-04-10')
        task_2 = ('panel dyskusyjny z klientem',1,1,project_id,'2021-03-21','2021-05-13')

        create_task(conn,task_1)
        create_task(conn,task_2)

if __name__ == '__main__':
    main()
