import mysql.connector as conn


cnx = conn.connect(user='root', passwd='MyUbuntu1604', db='aendb')
print(cnx.is_connected())
c = cnx.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS adresse(
          adresse_id INT UNSIGNED AUTO_INCREMENT,
          strasse VARCHAR(255),
          hnr VARCHAR(255),
          lkz CHAR(7),
          plz CHAR(9),
          ort VARCHAR(255),
          deleted TINYINT UNSIGNED NOT NULL DEFAULT 0,
          PRIMARY KEY(adressE_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS kunde(
                 kunde_id INT UNSIGNED AUTO_INCREMENT,
                 nachname VARCHAR(255),
                 vorname VARCHAR(255),
                 rechnung_adresse_id INT UNSIGNED,
                 lieger_adresse_id INT UNSIGNED,
                 bezahlart INT UNSIGNED NOT NULL DEFAULT 0,
                 art INT UNSIGNED NOT NULL DEFAULT 0,
                 deleted TINYINT UNSIGNED NOT NULL DEFAULT 0,
                 PRIMARY KEY(kunde_id)
                 )''')

c.execute("""CREATE TABLE IF NOT EXISTS bank(
        bank_id CHAR(12),
        bankname VARCHAR(255),
        lkz CHAR(2),
        deleted TINYINT UNSIGNED NOT NULL DEFAULT 0,
        PRIMARY KEY(bank_id))""")

c.execute("""CREATE TABLE IF NOT EXISTS bankverbindung(
        kunde_id INT UNSIGNED,
        bankverbindung_nr INT UNSIGNED,
        bank_id CHAR(12),
        kontonummer CHAR(25),
        iban CHAR(34),
        deleted TINYINT UNSIGNED NOT NULL DEFAULT 0,
        PRIMARY KEY(kunde_id, bankverbindung_nr)
        )""")



c.execute("""SHOW TABLES""")

l = c.fetchall()
for i in l:
    print(i[0])
    
c.execute('DESC kunde')
d = c.fetchall()
for i in d:
    print(i)
    
    
    
    
    
    
    
cnx.close()