# Module 8 - to do list

# TASK DESCRIPTION

# Import libraries
import sqlite3
from sys import argv

# Testing data


# Declare function
def setup():
    with sqlite3.connect('TODO_LIST.db') as connection_build:
        sql = '''CREATE TABLE task(
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                description VARCHAR(100) NOT NULL,
                is_done BOOL DEFAULT 0
            )'''
        sql2 = '''INSERT INTO task(description, is_done) VALUES ('Cook a dinner', 0), ('Take the rubbish out', 0), ('Go shopping', 1)'''
        cursor_build = connection_build.cursor()
        cursor_build.execute(sql)
        cursor_build.execute(sql2)
        connection_build.commit()


def tasks_status():
    tasks = cursor.execute('SELECT task_id, description FROM task WHERE is_done = 0')
    print("These are things to do:")
    for task in tasks:
        print(task)
    choice = int(input("What do u want to do?\n0 - Add new task\n1 - Print what I have to do already\nWhich operation u would like to perform? (If you want to exit program click Ctrl+C) "))
    return choice


# Tests
if len(argv) == 2 and argv[1] == 'setup':
    setup()

with sqlite3.connect('TODO_LIST.db') as connection:
    cursor = connection.cursor()
    while 0 == 0:
        decision = tasks_status()
        if decision == 0:
            new_task = str(input("What you should do? "))
            cursor.execute(f"INSERT INTO task(description, is_done) VALUES ('{new_task}', 0)")
        elif decision == 1:
            done_task = int(input("Write an ID of task you did: "))
            cursor.execute(f"UPDATE task SET is_done = 1 WHERE task_id = {done_task}")
        connection.commit()


# Print output message
