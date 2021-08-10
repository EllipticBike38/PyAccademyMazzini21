import sqlite3
if __name__=='__main__':
    lista=[('thor','odinson'),('loki','laufeyson'),('tony','stark'),('steve','rogers')]
    lista2=[('teschio','rosso'), ('Kang','The Conquerer'),('dormammu','/'),('loki','laufeyson')]
    db=sqlite3.connect('marulli_es7.db')
    db.execute('drop table if exists heroes')
    db.execute('create table heroes (id integer PRIMARY KEY, nome varchar(50), cognome varchar(50))')
    db.execute('drop table if exists villains')
    db.execute('create table villains (id integer PRIMARY KEY, nome varchar(50), cognome varchar(50))')
    db.execute('insert into heroes (id,nome, cognome) values (616, "bruce","banner")')
    for i in lista:
        db.execute('insert into heroes (nome, cognome) values (?,?)',i)
    for i in lista2:
        db.execute('insert into villains (nome, cognome) values (?,?)',i)
    db.commit()
    db.close()

    