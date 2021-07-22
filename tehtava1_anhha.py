import sqlite3

db = sqlite3.connect('kurssit.db')
db.isolation_level = None

c = db.cursor()

while True:
    # Valitse toiminto / Choose task by inputting corresponding tasks from 1 to 4:
    toimisto = input('Valitse toiminto: ')
    #1: Montako opintopistettä suoritettiin vuonna 2012 / How many credits were completed in 2012?
    if int(toimisto) == 1:
        vuosi = input('Anna vuosi: ')
        c.execute("SELECT sum(k.laajuus) FROM kurssit k LEFT JOIN suoritukset s on k.id= s.kurssi_id AND strftime('%Y', s.paivays) = ?",[vuosi])
        tiedot = c.fetchone()
        if tiedot[0] != None:
            print(f'opintopistettä suoritettiin: {tiedot[0]}')
            continue
        else:
            print('Valitse toisen vuosien')
            continue

    #2: Mikä on Hilkka Kuuselan viimeksi suorittaman kurssin koodi/ What is the code of Hilkka Kuusela's last course
    if int(toimisto) == 2:
        nimi = input('Anna opiskelijan nimi: ')
        c.execute("SELECT s.kurssi_id FROM suoritukset s, opiskelijat o WHERE o.id =s.opiskelija_id AND o.nimi = ? ORDER BY s.paivays DESC LIMIT 1;",[nimi])
        tiedot = c.fetchone()
        if tiedot[0] != None:
            print(f'Opiskelijan viimeksi suorittaman kurssin koodi: {tiedot[0]}')
            continue
        else:
            print('Kirjoitettaan toinen opiskelijan nimi')
            continue
     
     #3: Moniko opiskelija sai arvosanan 4 kurssilla TKT3433? / How many students received a grade of 4 in the course TKT3433?
    if int(toimisto) == 3:
        kurnimi = input('Anna kurssin nimi: ')
        c.execute("SELECT count(s.opiskelija_id) FROM suoritukset s join kurssit k on s.kurssi_id= k.id where k.nimi = ? and s.arvosana = 4;", [kurnimi])
        tiedot = c.fetchone()
        if tiedot[0] != None:
            print(f'Oppiskelijalaskea: : {tiedot[0]}')
            continue
        else:
            print('Kurssia ei löytynyt')
            continue 
    
    #4: Kuka on sijalla 11 opettajien top-listalla? / Who is ranked 11th on the top list of teachers?
    if int(toimisto) == 4:
        kuka = input('Anna opettajien top-listan maara: ')
        c.execute("SELECT O.nimi FROM Opettajat O LEFT JOIN kurssit k WHERE O.id = k.opettaja_id GROUP BY O.id ORDER BY SUM(k.laajuus) DESC LIMIT ?;", [kuka])
        tiedot = c.fetchall()
        if tiedot[10] != None:
            print(f'Opettaja sijalla 11 top-listalla: : {tiedot[10]}')
            continue
        else:
            print('kirjoitettaan toinen top-listaa')
            continue 
        
    # Break the loop and end program when choice is rather than 1-4.
    else:
        break
db.commit()
db.close()