import sqlite3
from iznimke import IznimkaPrazanTekst

con = sqlite3.connect("knjiznica.db")
cur = con.cursor()


def login_provjera(username, password):
    query = """
        SELECT id, username, password FROM admin;
    """
    data = cur.execute(query).fetchall()

    for d in data:
        if d[1] == username and d[2] == password:
            return False
