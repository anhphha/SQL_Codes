import sqlite3
import random 
from random import randint
import string
import secrets
import time 
import os 

os.system("rm elokuvat.db")
db = sqlite3.connect('elokuvat.db')
db.isolation_level = None


db.execute("CREATE TABLE teh3 (id INTEGER PRIMARY KEY, nimi TEXT, vuosi TIMESTAMP)")


#TEHTÄVÄ 2: Tauluun lisätään kyselyitä tehostava indeksi ennen rivien lisäämistä.
start3 = time.time()
n= 10**6

db.execute('BEGIN')
for i in range(n):
    db.execute('INSERT INTO teh3(nimi, vuosi) VALUES (?,?)', [random.choice(string.ascii_letters), random.randint(1990,2000)]) 
db.execute('COMMIT')

interval3 = time.time() - start3 

rivit2 = db.execute('SELECT id,nimi, vuosi from teh3').fetchall()
for rivi2 in rivit2:
 print(rivi2[0], rivi2[1],rivi2[2])

#TEHTÄVÄ 3: Tauluun lisätään kyselyitä tehostava indeksi ennen kyselyiden suoritusta.
# Elokuvien määrän laskemisessa käytä kyselyä indeksin kanssa
start4 = time.time()

db.execute('BEGIN')
maara2=db.execute("SELECT count(*) FROM teh3 WHERE vuosi = 1995").fetchone()
maara2 = maara2[0]
print(f'Vuonna 1995 julkaistun elokuvien määrän indeksin kanssa:', maara2)
db.execute('COMMIT')

interval4 = time.time() - start4
print(f'Rivien lisäämiseen kuluva aika indeksin kanssa:', round(interval3,2))
print(f'Kyselyiden suoritukseen kuluva aika indeksin kanssa:', round(interval4,2))
    