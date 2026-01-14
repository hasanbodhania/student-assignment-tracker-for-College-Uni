import sqlite3

DB_NAME = "assignments.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        title TEXT NOT NULL,
        due_date TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_assignment(subject, title, due_date, priority):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO assignments (subject, title, due_date, priority, status)
    VALUES (?, ?, ?, ?, 'Pending')
    """, (subject, title, due_date, priority))

    conn.commit()
    conn.close()


def get_all_assignments():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()

    conn.close()
    return rows


def mark_completed(assignment_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE assignments
    SET status = 'Completed'
    WHERE id = ?
    """, (assignment_id,))

    conn.commit()
    conn.close()
