import sqlite3

def new_connections_sqlite():
    db = sqlite3.connect("./database/app.db",check_same_thread=False)
    return db
