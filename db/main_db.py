import sqlite3
from datetime import datetime
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TASKS)
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute(queries.INSERT_TASKS, (task, created_at))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id, created_at


def get_task():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASKS)
    rows = cursor.fetchall()  
    conn.close()
    return rows


def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASKS, (new_task, task_id))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASKS, (task_id,))
    conn.commit()
    conn.close()