import sqlite3
import random
from random import randint 
import os 

os.system("rm Tehtava.db")
db=sqlite3.connect("Tehtava.db")
db.isolation_level = None

# c = db.cursor()

# Testi1 
db.execute("CREATE TABLE testi1 (x integer)")

# Ohjelma1:
suurin = db.execute('SELECT MAX(x) FROM Testi1').fetchone()
suurin = suurin[0]
print(f'Suurin arvo x', suurin)
db.execute("INSERT INTO Testi1(x) VALUES ({suurin + 1})")
rivit = db.execute('SELECT Count(*) FROM Testi1').fetchall()
rivit = rivit[0]
print(rivit[0])

#Ohjelma2:
for i in range(1,5000+1):
    db.execute('INSERT INTO Testi1(x) VALUES (?)', [i])



#Testi2
db.execute("CREATE TABLE testi1 (x integer Unique)")
for i in range(1,5000+1):
    db.execute('INSERT INTO Testi1(x) VALUES (?)', [i])
suurin = db.execute('SELECT MAX(x) FROM Testi1').fetchone()
suurin = suurin[0]
print(f'Suurin arvo x', suurin)
db.execute("INSERT INTO Testi1(x) VALUES (suurin + 1)")
rivit = db.execute('SELECT Count(*) FROM Testi1').fetchall()
rivit = rivit[0]
print(rivit[0])



#Testi 3
n=5000
db.execute('BEGIN')
for i in range(1, 5000+1):
    db.execute('INSERT INTO Testi1(x) VALUES (?)', [i])
rivit = db.execute('SELECT count(*) vuosi FROM testi1').fetchall()
rivit = rivit[0]
print(rivit[0])
suurin = db.execute('SELECT Max(*) FROM Testi1').fetchone()
suurin = suurin(0)
print(f'Suurin arvo x', suurin)
db.execute('BACKROLL')


