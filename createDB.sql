CREATE TABLE admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username CHAR(50) NOT NULL,
    password CHAR(50) NOT NULL
);

CREATE TABLE korisnik (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime CHAR(50) NOT NULL,
    prezime CHAR(50) NOT NULL,
    oib INT NOT NULL,
    adresa VARCHAR(100) NOT NULL
);

CREATE TABLE knjiga(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv VARCHAR(100) NOT NULL,
    autor CHAR(50) NOT NULL,
    izdavac CHAR(50) NOT NULL,
    godina_izdanja INT,
    polica CHAR(1),
    redak INT,
    stupac INT,
    stanje_id INT,
    FOREIGN KEY (stanje_id) REFERENCES stanje(id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE posudba(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    korisnik_id INTEGER,
    knjiga_id INTEGER,
    datum_posudbe DATE,
    zakasnina FLOAT,
    FOREIGN KEY (korisnik_id) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (knjiga_id) REFERENCES knjiga(id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE stanje(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dostupnost CHAR(50) NOT NULL
);

INSERT INTO admin (username, password) VALUES
    ('a', 'a');

INSERT INTO korisnik (ime, prezime, oib, adresa) VALUES
    ('Fran', 'Orlovic', 57456235920, 'Palinovecka 19H'),
    ('Iva', 'Radic', 12345678987, 'Goricanska 39');

INSERT INTO knjiga (naziv, autor, izdavac, godina_izdanja, polica, redak, stupac, stanje_id) VALUES
    ('Harry Potter i Red feniksa', 'J.K. Rowling', 'Lumin', '2003', 'A', 2, 3, 1),
    ('Harry Potter i Red feniksa', 'J.K. Rowling', 'Lumin', '2003', 'A', 2, 3, 1),
    ('Harry Potter i Red feniksa', 'J.K. Rowling', 'Lumin', '2003', 'A', 2, 3, 1),
    ('Harry Potter i Red feniksa', 'J.K. Rowling', 'Lumin', '2003', 'A', 2, 3, 1),
    ('Harry Potter i Red feniksa', 'J.K. Rowling', 'Lumin', '2003', 'A', 2, 3, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1),
    ('Harry Potter i Odaja tajni', 'J.K. Rowling', 'Lumin', '1998', 'A', 3, 1, 1);

INSERT INTO posudba (korisnik_id, knjiga_id, datum_posudbe, zakasnina) VALUES
    (1, 1, "10.07.2023.", 0),
    (2, 2, "10.07.2023.", 0);

INSERT INTO stanje (dostupnost) VALUES
    ('slobodno'),
    ('posudeno');