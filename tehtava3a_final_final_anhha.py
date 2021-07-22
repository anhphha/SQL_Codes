import sqlite3
import random
from random import randint
import string
import time
import secrets 

import os 

os.system("rm movies.db")


db = sqlite3.connect("movies.db")
db.isolation_level = None

# Tauluun ei lisätä kyselyitä tehostavaa indeksiä

db.execute("CREATE TABLE Elo27 (nimi TEXT, vuosi INTEGER)")
n=10**6

start1 = time.time()
db.execute('BEGIN')
for i in range(n):
	db.execute('INSERT INTO Elo27 (nimi, vuosi) VALUES (?, ?)', [secrets.token_bytes(8), random.randint(1990, 2000)])
db.execute('COMMIT')
interval1 = time.time() - start1



start2 = time.time()
vuosi = input('Anna vuosi: ')
for i in range(1000): 
	rivit = db.execute('SELECT vuosi, COUNT(*) FROM Elo27 WHERE vuosi = ? GROUP BY vuosi ORDER BY vuosi', [vuosi]).fetchall()
for rivi in rivit:
	print('Elokuvien maaran vuonna', rivi[0], rivi[1])
interval2= time.time()-start2


megatavua = db.execute('SELECT ((count(*)*(8+8))/1024/ 1024) FROM Elo27').fetchone()
print('Tietokantatiedoston koko testin lopuksi (megatavua)', megatavua[0])

print('Rivien lisaamiseen kuluva aika', interval1)
print('Kyselyiden suoritukseen kuluva aika', interval2)












#2. Tauluun lisätään kyselyitä tehostava indeksi ennen rivien lisäämistä.

#db.execute('CREATE INDEX idx_vuosi ON Elo1 (vuosi)')
#n=10**6
#db.execute('BEGIN')
#for i in range(n):
	#db.execute('INSERT INTO Elo2 (nimi, vuosi) VALUES (?, ?)', [random.choice(string.ascii_letters), random.randint(1990, 2000)])
#db.execute('COMMIT')

#rivit = db.execute('Select id, nimi, vuosi from Elo2').fetchall()
#for rivi in rivit:
	#print(rivi[0], rivi[1], rivi[2])

#maara2 = db.execute("EXPLAIN SELECT count(*) FROM Elo1 WHERE idx_vuosi = 5000")
#maara2 = maara2[0]
#print(maara2)


#3. Tauluun lisätään kyselyitä tehostava indeksi ennen kyselyiden suoritusta.

#n=10**6
#db.execute('BEGIN')
#for i in range(n):
	#db.execute('INSERT INTO Elo2 (nimi, vuosi) VALUES (?, ?)', [random.choice(string.ascii_letters), random.randint(1990, 2000)])
#db.execute('COMMIT')

#rivit = db.execute('Select id, nimi, vuosi from Elo2').fetchall()
#for rivi in rivit:
	#print(rivi[0], rivi[1], rivi[2])

#db.execute('CREATE INDEX idx_vuosi ON Elo1 (vuosi)')
#maara2 = db.execute("EXPLAIN SELECT count(*) FROM Elo1 WHERE idx_vuosi = 5000")
#maara2 = maara2[0]
#print(maara2)

db.commit()
db.close()
