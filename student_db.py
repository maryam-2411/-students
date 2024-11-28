import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''create table if not exists students
                         (id integer primary key,
                         fname text,
                         lname text,
                         name_c text,
                         password integer)''')
        self.con.commit()

    def show(self):
        self.cur.execute("select * from students")
        records = self.cur.fetchall()
        return records
    
    def add(self,fname,lname,name_c,password):
        self.cur.execute('insert into students values(null,?,?,?,?)',(fname,lname,name_c,password))
        self.con.commit()

    def delete(self,fname):
        self.cur.execute('delete from students where fname =?',(fname,))
        self.con.commit()

    def search(self,password):
        self.cur.execute("select password from students where password = ?",(password,))
        record = self.cur.fetchall()
        return record
              
        