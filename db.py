import sqlite3

DB_FILE = "monitor.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

# Whenever we want to communicate with the db, we need to open a connection, which is returned
def get_connection():
    return sqlite3.connection(DB_FILE)


def init_db():
    # connect to the db, that we want to execute sql commands on
    conn = get_connection()
    # cursor acts like a text input, allowing the running of sql commands in python
    cur = conn.cursor()
    # execute these sql commands, which creates the db table with id, url, is_active, and check_interval
    # the primary key autoincrement makes it increment when another is added
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL UNIQUE,
                is_active INTEGER DEFAULT 1,
                check_interval INTEGER DEFAULT 5
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_id INTEGER NOT NULL,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
                FOREIGN KEY (site_id) REFERENCES sites(id)
                )
""")
    # commit saves
    conn.commit()
    #close the connection, obviously
    conn.close()

def add_site(url, check_interval=5):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO sites (url, check_interval) VALUES(?,?)", (url, check_interval))
        cur.commit()
    except sqlite3.IntegrityError:
        print(f"Duplicate Site '{url}'.")
    finally:
        conn.close()
def remove_site(url):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM sites WHERE url = ?", (url))
        cur.commit()
    except sqlite3.IntegrityError:
        print(f"No matching site to '{url}'.")
    finally:
        conn.close()
def list_sites():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, url, is_active, check_interval FROM sites")
    output = cur.fetchall()
    conn.close()
    return output

def toggle_monitor_on(url):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE sites SET is_active = ? WHERE url = ?", (1, url))
    cur.execute("")

def toggle_monitor_off(url):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE sites SET is_active = ? WHERE url = ?", (0, url))
    cur.execute("") 

def monitor()

    

