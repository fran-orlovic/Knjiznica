import sqlite3
from iznimke import IznimkaPrazanTekst

con = sqlite3.connect("knjiznica.db")
cur = con.cursor()


def novi_korisnik_provjera(ime, prezime, oib, adresa):
    query = """
        SELECT * from korisnik ORDER BY prezime
    """
    korisnik = cur.execute(query).fetchall()

    try:
        if len(ime) == 0 or len(prezime) == 0 or len(oib) == 0 or len(adresa) == 0:
            raise IznimkaPrazanTekst()

        if isinstance(int(oib), int) is False:
            raise Exception(f"OIB mora biti broj!")

    except IznimkaPrazanTekst as e:
        return str(e)

    except Exception as e:
        return str(e)


def login_provjera(username, password):
    query = """
        SELECT id, username, password FROM admin;
    """
    data = cur.execute(query).fetchall()

    for d in data:
        if d[1] == username and d[2] == password:
            return False
