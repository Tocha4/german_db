import mysql.connector 


cnx = mysql.connector.connect(user='root', passwd='MyUbuntu1604')

c = cnx.cursor()

c.execute('''CREATE SCHEMA IF NOT EXISTS aendb
           CHARACTER SET utf8
           COLLATE utf8_unicode_ci''')



c.execute('SHOW SCHEMAS')
l = c.fetchall()
for i in l:
    print(i[0])



c.execute('''DROP SCHEMA aendb''')


c.execute('SHOW SCHEMAS')
l = c.fetchall()
for i in l:
    print(i[0])



cnx.close()