from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

from utilities import login_provjera

con = sqlite3.connect("knjiznica.db")
cur = con.cursor()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Knjižnica")
        self.setWindowIcon(QtGui.QIcon('images/knjige.png'))
        self.setGeometry(1600, 100, 900, 600)
        self.initUi()

    def initUi(self):

        # LOGIN WINDOW #
        # frame_login
        self.frame_login = QtWidgets.QFrame(self)
        self.frame_login.setGeometry(QtCore.QRect(250, 100, 300, 300))
        self.frame_login.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_login)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 0, 200, 200))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # label_login
        self.label_login = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_login.setText("Welcome!")
        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 2, QtCore.Qt.AlignCenter)

        # label_username
        self.label_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_username.setText("Username")
        self.label_username.setMinimumSize(50, 30)
        self.gridLayout.addWidget(self.label_username, 1, 0, 1, 1)

        # text_username
        self.text_username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.text_username.setMaximumSize(150, 20)
        self.gridLayout.addWidget(self.text_username, 1, 1, 1, 1)

        # label_password
        self.label_password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_password.setText("Password")
        self.label_password.setMinimumSize(50, 30)
        self.gridLayout.addWidget(self.label_password, 3, 0, 1, 1)

        # text_password
        self.text_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.text_password, 3, 1, 1, 1)

        # button_login
        self.button_login = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_login.setText("Sign in")
        self.button_login.clicked.connect(self.login_check)
        self.gridLayout.addWidget(self.button_login, 5, 0, 1, 2)

        # label_error_login
        self.label_error_login = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_error_login.setMinimumSize(50, 30)
        self.label_error_login.setStyleSheet("color:red;")
        self.gridLayout.addWidget(self.label_error_login, 6, 0, 1, 2, QtCore.Qt.AlignCenter)
        # LOGIN WINDOW END #

        # MENU WINDOW #
        # frame_menu
        self.frame_menu = QtWidgets.QFrame(self)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 510, 30))
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 30))
        self.horizontalLayout_menu = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_menu.setContentsMargins(0, 0, 0, 0)

        # button_korisnici
        self.button_korisnici = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_korisnici.setText("Korisnici")
        self.button_korisnici.clicked.connect(self.korisnici_frame)
        self.horizontalLayout_menu.addWidget(self.button_korisnici)

        # button_knjige
        self.button_knjige = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_knjige.setText("Knjige")
        self.button_knjige.clicked.connect(self.knjige_frame)
        self.horizontalLayout_menu.addWidget(self.button_knjige)

        # button_skladiste
        self.button_skladiste = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_skladiste.setText("Skladište")
        self.button_skladiste.clicked.connect(self.skladiste_frame)
        self.horizontalLayout_menu.addWidget(self.button_skladiste)
        # MENU WINDOW END #

        # KORISNICI WINDOW #
        # frame_korisnici_podaci
        self.frame_korisnici_podaci = QtWidgets.QFrame(self)
        self.frame_korisnici_podaci.setGeometry(QtCore.QRect(10, 35, 810, 470))
        self.frame_korisnici_podaci.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_korisnici_podaci.setFrameShadow(QtWidgets.QFrame.Raised)

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_korisnici_podaci)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 300, 90))

        self.gridLayout_search = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_search.setContentsMargins(0, 0, 0, 0)

        # label_search
        self.label_search = QtWidgets.QLabel(self)
        self.label_search.setText("Pretraži")
        self.label_search.setMaximumWidth(50)
        self.gridLayout_search.addWidget(self.label_search, 0, 0, 1, 1)

        # text_search
        self.text_search = QtWidgets.QLineEdit(self)
        self.text_search.setFixedHeight(20)
        self.text_search.setMinimumWidth(200)
        self.text_search.textChanged.connect(self.search_korisnika)
        self.gridLayout_search.addWidget(self.text_search, 0, 1, 1, 1, QtCore.Qt.AlignLeft)

        # button_search -> TODO: ne treba ako koristis EVENT za povezivanje (Antolic na teamsu)
        # self.button_search = QtWidgets.QPushButton(self.gridLayoutWidget)
        # self.button_search.setMaximumSize(50, 25)
        # self.gridLayout_search.addWidget(self.button_search, 1, 1, 1, 1)

        # scrollArea korisnici
        self.scrollArea_korisnici = QtWidgets.QScrollArea(self.frame_korisnici_podaci)
        self.scrollArea_korisnici.setGeometry(QtCore.QRect(10, 60, 380, 260))
        self.scrollArea_korisnici.setWidgetResizable(True)
        # listView korisnici
        self.listView_korisnici = QtWidgets.QListWidget(self)
        self.scrollArea_korisnici.setWidget(self.listView_korisnici)

        # button odabir korisnika za posudbu
        self.button_odabir_korisnika = QtWidgets.QPushButton(self.frame_korisnici_podaci)
        self.button_odabir_korisnika.setText("Odaberi korisnika")
        self.button_odabir_korisnika.setGeometry(QtCore.QRect(10, 350, 100, 25))

        # button unos novog korisnika
        self.button_novi_korisnik = QtWidgets.QPushButton(self.frame_korisnici_podaci)
        self.button_novi_korisnik.setText("Unos novog korisnika")
        self.button_novi_korisnik.setGeometry(QtCore.QRect(270, 350, 120, 25))
        self.button_novi_korisnik.clicked.connect(self.unos_novog_korisnika_window)

        # frame_stanje_posudbi
        self.frame_stanje_posudbi = QtWidgets.QFrame(self.frame_korisnici_podaci)
        self.frame_stanje_posudbi.setGeometry(QtCore.QRect(460, 0, 400, 550))
        self.frame_stanje_posudbi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stanje_posudbi.setFrameShadow(QtWidgets.QFrame.Raised)

        # label_posudeno
        self.label_posudeno = QtWidgets.QLabel(self.frame_stanje_posudbi)
        self.label_posudeno.setText("Posuđeno")
        self.label_posudeno.setGeometry(QtCore.QRect(0, 0, 50, 25))

        # scrollArea_posudeno
        self.scrollArea_posudeno = QtWidgets.QScrollArea(self.frame_stanje_posudbi)
        self.scrollArea_posudeno.setGeometry(QtCore.QRect(0, 30, 320, 180))
        self.scrollArea_posudeno.setWidgetResizable(True)
        self.listView_posudeno = QtWidgets.QListWidget(self)
        self.scrollArea_posudeno.setWidget(self.listView_posudeno)

        # button_vracanje_knjige
        self.button_vracanje_knjige = QtWidgets.QPushButton(self.frame_stanje_posudbi)
        self.button_vracanje_knjige.setText("Vraćanje knjige")
        self.button_vracanje_knjige.setGeometry(QtCore.QRect(100, 230, 120, 25))

        # label_vraceno
        self.label_vraceno = QtWidgets.QLabel(self.frame_stanje_posudbi)
        self.label_vraceno.setText("Vraćeno")
        self.label_vraceno.setGeometry(QtCore.QRect(0, 250, 50, 25))

        # scrollArea_vraceno
        self.scrollArea_vraceno = QtWidgets.QScrollArea(self.frame_stanje_posudbi)
        self.scrollArea_vraceno.setGeometry(QtCore.QRect(0, 280, 320, 180))
        self.scrollArea_vraceno.setWidgetResizable(True)
        self.listView_vraceno = QtWidgets.QListWidget(self)
        self.scrollArea_vraceno.setWidget(self.listView_vraceno)

        # frame_unos_novog_korisnika
        self.frame_unos_novog_korisnika = QtWidgets.QFrame(self.frame_korisnici_podaci)
        self.frame_unos_novog_korisnika.setGeometry(QtCore.QRect(460, 80, 400, 550))
        self.frame_unos_novog_korisnika.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_unos_novog_korisnika.setFrameShadow(QtWidgets.QFrame.Raised)

        # gridLayout_novi_korisnik
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_unos_novog_korisnika)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 200, 200))
        self.gridLayout_novi_korisnik = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_novi_korisnik.setContentsMargins(0, 0, 0, 0)

        # label_ime
        self.label_ime = QtWidgets.QLabel(self)
        self.label_ime.setText("Ime")
        self.gridLayout_novi_korisnik.addWidget(self.label_ime, 0, 0, 1, 1)

        # text_ime
        self.text_ime = QtWidgets.QLineEdit(self)
        self.text_ime.setFixedHeight(25)
        self.text_ime.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_novi_korisnik.addWidget(self.text_ime, 0, 1, 1, 1)

        # label_prezime
        self.label_prezime = QtWidgets.QLabel(self)
        self.label_prezime.setText("Prezime")
        self.gridLayout_novi_korisnik.addWidget(self.label_prezime, 1, 0, 1, 1)

        # text_prezime
        self.text_prezime = QtWidgets.QLineEdit(self)
        self.text_prezime.setFixedHeight(25)
        self.text_prezime.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_novi_korisnik.addWidget(self.text_prezime, 1, 1, 1, 1)

        # label_oib
        self.label_oib = QtWidgets.QLabel(self)
        self.label_oib.setText("OIB")
        self.gridLayout_novi_korisnik.addWidget(self.label_oib, 2, 0, 1, 1)

        # text_oib
        self.text_oib = QtWidgets.QLineEdit(self)
        self.text_oib.setFixedHeight(25)
        self.text_oib.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_novi_korisnik.addWidget(self.text_oib, 2, 1, 1, 1)

        # label_adresa
        self.label_adresa = QtWidgets.QLabel(self)
        self.label_adresa.setText("Adresa")
        self.gridLayout_novi_korisnik.addWidget(self.label_adresa, 3, 0, 1, 1)

        # text_adresa
        self.text_adresa = QtWidgets.QLineEdit(self)
        self.text_adresa.setFixedHeight(25)
        self.text_adresa.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_novi_korisnik.addWidget(self.text_adresa, 3, 1, 1, 1)

        # button_dovrsi_unos
        self.button_dovrsi_unos = QtWidgets.QPushButton(self.frame_unos_novog_korisnika)
        self.button_dovrsi_unos.setText("Dovrši unos")
        # TODO: Dodati connect za unos u listu
        self.gridLayout_novi_korisnik.addWidget(self.button_dovrsi_unos, 4, 0, 1, 2)

        # button_natrag
        self.button_natrag = QtWidgets.QPushButton(self.frame_unos_novog_korisnika)
        self.button_natrag.setText("Natrag")
        self.button_natrag.clicked.connect(self.stanje_posudbi_window)
        # self.button_natrag.setFixedHeight(25)
        self.gridLayout_novi_korisnik.addWidget(self.button_natrag, 5, 0, 1, 1)

        # KORISNICI WINDOW END #

        # KNJIGE WINDOW #

        # frame_posudba
        self.frame_posudba = QtWidgets.QFrame(self)
        self.frame_posudba.setGeometry(QtCore.QRect(10, 35, 810, 500))
        self.frame_posudba.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_posudba.setFrameShadow(QtWidgets.QFrame.Raised)

        # gridLayout_pretraga_knjige
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_posudba)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 380, 60))
        self.gridLayout_pretraga_knjige = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_pretraga_knjige.setContentsMargins(0, 0, 0, 0)

        # label_knjige_search
        self.label_knjige_search = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_knjige_search.setText("Pretraži")
        self.gridLayout_pretraga_knjige.addWidget(self.label_knjige_search, 0, 0, 1, 1)

        # text_knjige_search
        self.text_knjige_search = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout_pretraga_knjige.addWidget(self.text_knjige_search, 0, 1, 1, 1)

        # scrollArea_knjige
        self.scrollArea_knjige = QtWidgets.QScrollArea(self.frame_posudba)
        self.scrollArea_knjige.setGeometry(QtCore.QRect(10, 80, 380, 260))
        self.scrollArea_knjige.setWidgetResizable(True)
        # listView_knjige
        self.listView_knjige = QtWidgets.QListWidget(self)
        self.scrollArea_knjige.setWidget(self.listView_knjige)

        # gridLayout_polica
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_posudba)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(400, 50, 400, 290))
        self.gridLayout_polica = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_polica.setContentsMargins(0, 0, 0, 0)

        # label_naziv_police
        self.label_naziv_police = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_naziv_police.setText("Polica")
        self.label_naziv_police.setMaximumSize(400, 25)
        self.label_naziv_police.setStyleSheet("border: 1px solid black;")
        self.gridLayout_polica.addWidget(self.label_naziv_police, 0, 0, 1, 6)

        # polica_1_1
        self.label_polica11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica11.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica11, 1, 1, 1, 1)

        # polica_1_2
        self.label_polica12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica12.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica12, 1, 2, 1, 1)

        # polica_1_3
        self.label_polica13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica13.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica13, 1, 3, 1, 1)

        # polica_1_4
        self.label_polica14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica14.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica14, 1, 4, 1, 1)

        # polica_1_5
        self.label_polica15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica15.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica15, 1, 5, 1, 1)

        # polica_2_1
        self.label_polica21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica21.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica21, 2, 1, 1, 1)

        # polica_2_2
        self.label_polica22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica22.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica22, 2, 2, 1, 1)

        # polica_2_3
        self.label_polica23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica23.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica23, 2, 3, 1, 1)

        # polica_2_4
        self.label_polica24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica24.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica24, 2, 4, 1, 1)

        # polica_2_5
        self.label_polica25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica25.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica25, 2, 5, 1, 1)

        # polica_3_1
        self.label_polica31 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica31.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica31, 3, 1, 1, 1)

        # polica_3_2
        self.label_polica32 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica32.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica32, 3, 2, 1, 1)

        # polica_3_3
        self.label_polica33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica33.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica33, 3, 3, 1, 1)

        # polica_3_4
        self.label_polica34 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica34.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica34, 3, 4, 1, 1)

        # polica_3_5
        self.label_polica35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica35.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica35, 3, 5, 1, 1)

        # polica_4_1
        self.label_polica41 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica41.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica41, 4, 1, 1, 1)

        # polica_4_2
        self.label_polica42 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica42.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica42, 4, 2, 1, 1)

        # polica_4_3
        self.label_polica43 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica43.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica43, 4, 3, 1, 1)

        # polica_4_4
        self.label_polica44 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica44.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica44, 4, 4, 1, 1)

        # polica_4_5
        self.label_polica45 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica45.setStyleSheet("border: 1px solid blue;")
        self.gridLayout_polica.addWidget(self.label_polica45, 4, 5, 1, 1)

        # gridLayout_posudba
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_posudba)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 400, 300, 80))
        self.gridLayout_posudba = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_posudba.setContentsMargins(0, 0, 0, 0)

        # button_odabir_knjige
        self.button_odabir_knjige = QtWidgets.QPushButton(self.frame_posudba)
        self.button_odabir_knjige.setText("Odaberi knjigu")
        self.button_odabir_knjige.setGeometry(QtCore.QRect(10, 350, 100, 25))

        # label_posudba_korisnik
        self.label_posudba_korisnik = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_posudba_korisnik.setText("Odabrani korisnik")
        self.gridLayout_posudba.addWidget(self.label_posudba_korisnik, 0, 0, 1, 1)

        # label_odabrani_korisnik
        self.label_odabrani_korisnik = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_odabrani_korisnik.setStyleSheet("background-color: white")
        self.label_odabrani_korisnik.setMaximumWidth(100)
        self.gridLayout_posudba.addWidget(self.label_odabrani_korisnik, 0, 1, 1, 1)

        # label_posudba_knjiga
        self.label_posudba_knjiga = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_posudba_knjiga.setText("Odabrana knjiga")
        self.gridLayout_posudba.addWidget(self.label_posudba_knjiga, 1, 0, 1, 1)

        # label_odabrana_knjiga
        self.label_odabrana_knjiga = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_odabrana_knjiga.setStyleSheet("background-color: white")
        self.label_odabrana_knjiga.setMinimumWidth(250)
        self.gridLayout_posudba.addWidget(self.label_odabrana_knjiga, 1, 1, 1, 1)

        # button_potvrda_posudbe
        self.button_potvrda_posudbe = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.button_potvrda_posudbe.setText("Potvrdi posudbu")
        self.gridLayout_posudba.addWidget(self.button_potvrda_posudbe, 2, 0, 1, 2)

        # KNJIGE WINDOW END #

        # SKLADISTE WINDOW #
        self.frame_skladiste = QtWidgets.QFrame(self)
        self.frame_skladiste.setGeometry(QtCore.QRect(10, 30, 800, 500))
        self.frame_skladiste.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_skladiste.setFrameShadow(QtWidgets.QFrame.Raised)

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_skladiste)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 300, 60))

        self.gridLayout_pretraga_knjige = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_pretraga_knjige.setContentsMargins(0, 0, 0, 0)

        # label knjige_search_skladiste
        self.label_knjige_search_skladiste = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_knjige_search_skladiste.setText("Pretraži")
        self.gridLayout_pretraga_knjige.addWidget(self.label_knjige_search_skladiste, 0, 0, 1, 1)

        # text knjige_search_skladiste
        self.text_knjige_search_skladiste = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout_pretraga_knjige.addWidget(self.text_knjige_search_skladiste, 0, 1, 1, 1)

        # scrollArea_knjige_skladiste
        self.scrollArea_knjige_skladiste = QtWidgets.QScrollArea(self.frame_skladiste)
        self.scrollArea_knjige_skladiste.setGeometry(QtCore.QRect(20, 80, 400, 300))
        self.scrollArea_knjige_skladiste.setWidgetResizable(True)

        # listView_knjige_skladiste
        self.listView_knjige_skladiste = QtWidgets.QListWidget(self)
        self.scrollArea_knjige_skladiste.setWidget(self.listView_knjige_skladiste)

        # gridLayout_nova_knjiga
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_skladiste)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(450, 70, 250, 300))
        self.gridLayout_nova_knjiga = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.setContentsMargins(0, 0, 0, 0)

        # label_unos_nove_knjige
        self.label_unos_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_unos_nove_knjige.setText("Unos nove knjige")
        self.gridLayout_nova_knjiga.addWidget(self.label_unos_nove_knjige, 0, 0, 1, 2, QtCore.Qt.AlignCenter)
        self.label_unos_nove_knjige.setMaximumHeight(25)

        # label_naziv_nove_knjige
        self.label_naziv_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_naziv_nove_knjige.setText("Naziv")
        self.gridLayout_nova_knjiga.addWidget(self.label_naziv_nove_knjige, 1, 0, 1, 1)

        # text_naziv_nove_knjige
        self.text_naziv_nove_knjige = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.text_naziv_nove_knjige, 1, 1, 1, 1)

        # label_autor_nove_knjige
        self.label_autor_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_autor_nove_knjige.setText("Autor")
        self.gridLayout_nova_knjiga.addWidget(self.label_autor_nove_knjige, 2, 0, 1, 1)

        # text_autor_nove_knjige
        self.text_autor_nove_knjige = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.text_autor_nove_knjige, 2, 1, 1, 1)

        # label_izdavac_nove_knjige
        self.label_izdavac_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_izdavac_nove_knjige.setText("Izdavač")
        self.gridLayout_nova_knjiga.addWidget(self.label_izdavac_nove_knjige, 3, 0, 1, 1)

        # text_izdavac_nove_knjige
        self.text_izdavac_nove_knjige = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.text_izdavac_nove_knjige, 3, 1, 1, 1)

        # label_godina_nove_knjige
        self.label_godina_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_godina_nove_knjige.setText("Godina izdanja")
        self.gridLayout_nova_knjiga.addWidget(self.label_godina_nove_knjige, 4, 0, 1, 1)

        # text_godina_nove_knjige
        self.text_godina_nove_knjige = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.text_godina_nove_knjige, 4, 1, 1, 1)
        self.text_godina_nove_knjige.setMaximumWidth(50)

        # label_kolicina_nove_knjige
        self.label_kolicina_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_kolicina_nove_knjige.setText("Količina")
        self.gridLayout_nova_knjiga.addWidget(self.label_kolicina_nove_knjige, 5, 0, 1, 1)

        # text_kolicina_nove_knjige
        self.text_kolicina_nove_knjige = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.text_kolicina_nove_knjige, 5, 1, 1, 1)
        self.text_kolicina_nove_knjige.setMaximumWidth(50)

        # label_polica
        self.label_polica = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_polica.setText("Polica")
        self.gridLayout_nova_knjiga.addWidget(self.label_polica, 6, 0, 1, 1)

        # comboBox_polica_nove_knjige
        self.comboBox_polica_nove_knjige = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.comboBox_polica_nove_knjige, 6, 1, 1, 1)

        # label_redak_nove_knjige
        self.label_redak_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_redak_nove_knjige.setText("Redak")
        self.gridLayout_nova_knjiga.addWidget(self.label_redak_nove_knjige, 7, 0, 1, 1)

        # comboBox_redak
        self.comboBox_redak = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.comboBox_redak, 7, 1, 1, 1)

        # label_stupac_nove_knjige
        self.label_stupac_nove_knjige = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_stupac_nove_knjige.setText("Stupac")
        self.gridLayout_nova_knjiga.addWidget(self.label_stupac_nove_knjige, 8, 0, 1, 1)

        # comboBox_stupac
        self.comboBox_stupac = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.gridLayout_nova_knjiga.addWidget(self.comboBox_stupac, 8, 1, 1, 1)

        # button_potvrdi_unos
        self.button_potvrdi_unos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_potvrdi_unos.setText("Potvrdi unos nove knjige")
        self.gridLayout_nova_knjiga.addWidget(self.button_potvrdi_unos, 9, 0, 1, 2)

        # SKLADISTE WINDOW END #
        self.frame_menu.hide()
        #self.frame_login.hide()
        self.frame_korisnici_podaci.hide()
        self.frame_unos_novog_korisnika.hide()
        self.frame_posudba.hide()
        self.frame_skladiste.hide()

    def login_check(self):
        error_login = login_provjera(self.text_username.text(), self.text_password.text())
        if error_login is None:
            if len(self.text_username.text()) == 0 or len(self.text_password.text()) == 0:
                self.label_error_login.setText("Niste unijeli sve podatke!")
            else:
                self.label_error_login.setText("Neispravan username i/ili password!")

        elif error_login is False:
            self.label_error_login.setText("")
            self.frame_login.hide()
            self.frame_menu.show()
            self.frame_korisnici_podaci.show()
            query_korisnici = """
                SELECT korisnik_id, ime, prezime, oib, adresa, zakasnina FROM posudba
                LEFT JOIN korisnik ON korisnik.id = posudba.korisnik_id
            """
            korisnici = cur.execute(query_korisnici).fetchall()
            for korisnik in korisnici:
                self.listView_korisnici.insertItem(1, f"{korisnik[0]}. {korisnik[1]} {korisnik[2]}, {korisnik[3]}, "
                                                      f"{korisnik[4]}, {korisnik[5]} €")

            query_knjige = """
                SELECT naziv, autor, izdavac, godina_izdanja, stanje_id FROM knjiga ORDER BY naziv DESC
            """
            knjige = cur.execute(query_knjige).fetchall()
            for knjiga in knjige:
                if knjiga[4] == 1:
                    self.listView_knjige.insertItem(0, f"{knjiga[0]}, {knjiga[1]}, {knjiga[2]}, {knjiga[3]}")

            query_skladiste = """
                SELECT naziv, autor, izdavac, godina_izdanja FROM knjiga ORDER BY naziv DESC
            """
            skladiste = cur.execute(query_skladiste).fetchall()
            prev_knjiga = 0
            broj_knjiga = 0
            for i, podatak in enumerate(skladiste, start=1):
                if prev_knjiga == 0:
                    prev_knjiga = podatak[0]
                    broj_knjiga += 1
                elif prev_knjiga != podatak[0]:
                    self.listView_knjige_skladiste.insertItem(0, f"{prev_knjiga}, {podatak[1]}, {podatak[2]}, "
                                                                 f"{broj_knjiga}")
                    prev_knjiga = podatak[0]
                    broj_knjiga = 1
                else:
                    broj_knjiga += 1
                    if i == len(skladiste):
                        self.listView_knjige_skladiste.insertItem(0, f"{podatak[0]}, {podatak[1]}, {podatak[2]}, "
                                                                     f"{broj_knjiga}")

    def search_korisnika(self):
        query_search_korisnika = """
            SELECT korisnik_id, ime, prezime, oib, adresa, zakasnina FROM posudba
            LEFT JOIN korisnik ON korisnik.id = posudba.korisnik_id ORDER BY korisnik_id DESC
        """
        korisnici = cur.execute(query_search_korisnika).fetchall()
        self.listView_korisnici.clear()
        for korisnik in korisnici:
            if self.text_search.text() == "":
                self.listView_korisnici.insertItem(0, f"{korisnik[0]}. {korisnik[1]} {korisnik[2]}, {korisnik[3]}, "
                                                      f"{korisnik[4]}, {korisnik[5]} €")
            elif self.text_search.text() == korisnik[1]:
                self.listView_korisnici.insertItem(0, f"{korisnik[0]}. {korisnik[1]} {korisnik[2]}, {korisnik[3]}, "
                                                      f"{korisnik[4]}, {korisnik[5]} €")
            elif self.text_search.text() == korisnik[2]:
                self.listView_korisnici.insertItem(0, f"{korisnik[0]}. {korisnik[1]} {korisnik[2]}, {korisnik[3]}, "
                                                      f"{korisnik[4]}, {korisnik[5]} €")
            elif self.text_search.text() == str(korisnik[3]):
                self.listView_korisnici.insertItem(0, f"{korisnik[0]}. {korisnik[1]} {korisnik[2]}, {korisnik[3]}, "
                                                      f"{korisnik[4]}, {korisnik[5]} €")
            elif self.text_search.text() == korisnik[4]:
                self.listView_korisnici.insertItem(0, f"{korisnik[0]}. {korisnik[1]} {korisnik[2]}, {korisnik[3]}, "
                                                      f"{korisnik[4]}, {korisnik[5]} €")

    def korisnici_frame(self):
        self.frame_posudba.hide()
        self.frame_skladiste.hide()
        self.frame_korisnici_podaci.show()

    def knjige_frame(self):
        self.frame_skladiste.hide()
        self.frame_korisnici_podaci.hide()
        self.frame_posudba.show()

    def skladiste_frame(self):
        self.frame_korisnici_podaci.hide()
        self.frame_posudba.hide()
        self.frame_skladiste.show()

    def unos_novog_korisnika_window(self):
        self.frame_unos_novog_korisnika.show()
        self.frame_stanje_posudbi.hide()

    def stanje_posudbi_window(self):
        self.frame_stanje_posudbi.show()
        self.frame_unos_novog_korisnika.hide()


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
