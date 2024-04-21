import sqlite3
import random

sq = sqlite3.connect('casino.db')
sql = sq.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS casino (
                    
    login VARCHAR (55),
    password VARCHAR (55),
    cash INT        
            
            )""")


print('xos geldin casinoya!')

while True:

    choice = input('Choice: (1) qeydiyyat (2) oyna (3) istifadeci sil (4) balans (5) cix: ')

    if choice == '1':
        login = input(' daxil et login (ancaq herf ve reqem): ')
        password = input('daxil et password  (ancaq herf ve reqem): ')
        cash = int(input(' pul məbləğinizi daxil edin: '))
        sql.execute('INSERT INTO casino (login, password, cash) VALUES (?, ?, ?)', (login, password, cash))
        sq.commit()
        print('qeydiyyat ugurlu!')

    elif choice == '2':
        balance = sql.execute('SELECT cash FROM casino WHERE login=?', (login,)).fetchone()[0]
        if balance < 5:
            print('Yetərsiz vəsait')
        else:
            result = random.choice(['win', 'lose'])
            if result == 'win':
                print('tebrikler 10 azn qazandiniz')
                balance += 10
            else:
                print('itirdiniiz 5 azn')
                balance -= 5
            sql.execute('UPDATE casino SET cash=? WHERE login=?', (balance, login))
            sq.commit()

    elif choice == '3':
        while True:
            check1 = input('Are you sure? y/n: ')
            if check1 == 'y':
                sql.execute('DELETE FROM casino WHERE login=?', (login,))
                sq.commit()
                print('İstifadəçi verilənlər bazasından silindi')
                login = None 
                break  
            elif check1 == 'n':
                print('aliyyətlərin ləğvi. Seçim menyusuna qayıdın')
                break 
            else:
                print('Etibarsız seçim. Zəhmət olmasa y/n daxil edin.')
                continue  

    elif choice == '4':
        balance = sql.execute('SELECT cash FROM casino WHERE login=?', (login,)).fetchone()
        if balance:
            print(f'Cari balansınız {balance[0]} azn')
        else:
            print('istifadeci yoxdur.')

    elif choice == '5':
        print('Oyundan çıxır...')
        break
    
    else:
        print('Yanlış seçim. Yenidən cəhd elə.')