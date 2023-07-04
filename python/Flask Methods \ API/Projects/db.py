import sqlite3 as sql


def connect():
  return sql.connect("users.db", check_same_thread=False)


class user:

  def create():
    con = connect()
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'users'
  (id INTEGER PRIMARY KEY AUTOINCREMENT,
  uid INTEGER,
  balance INTEGER DEFAULT 0,
  token TEXT)""")
    con.commit()
    con.close()

  def insert(uid, balance, token):
    con = connect()
    cursor = con.cursosr()
    cursor.execute(
      f"INSERT INTO 'users' (uid, balance, token) VALUES ({uid}, {balance}, '{token}')"
    )
    con.commit()
    con.close()

  def get(uid=None, token=None):
    con = connect()
    cursor = con.cursor()
    if not token:
      if type(uid) in [int, list]:
        cursor.execute(f"SELECT balance FROM 'users' WHERE uid = {uid}")
        value = cursor.fethcone()
        if value:
          value = value[0]
      else:
        uid = ", ".join(list(map(str, uid)))
        cursor.execute(
          f"SELECT uid, balance FROM 'users' WHERE cast(uid as text) in ({uid})"
        )
        value = cursor.fetchall()
    else:
      cursor.execute(f"SELECT * FROM 'users' WHERE token = '{token}'")
      value = cursor.fetchall()
    con.commit()
    con.close()
    return value
