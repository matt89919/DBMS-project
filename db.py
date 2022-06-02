import sqlite3

class Datebase:
    def __init__(self, db):
        self.connection=sqlite3.connect(db)
        self.cursor=self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS teams (name text PRIMARY KEY, city text, arena text, owner text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS players (SSN text PRIMARY KEY, name text, team text, school text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS coaches (SSN text PRIMARY KEY, name text, team text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contracts (SSN text PRIMARY KEY, value INTEGER, length INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS schools (name text PRIMARY KEY, location text, ranking INTEGER)")
        self.connection.commit()

    def fetch(self, table):
        cmd="SELECT * FROM "+table
        self.cursor.execute(cmd)
        rows=self.cursor.fetchall()
        return rows

    def insertteam(self, name, city, arena, owner):
        cmd="INSERT INTO teams VALUES ('"+name+"', '"+city+"', '"+arena+"', '"+owner+"')"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def insertplayer(self, ssn, name, team, school):
        cmd="INSERT INTO players VALUES ('"+ssn+"', '"+name+"', '"+team+"', '"+school+"')"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def insertcoach(self, ssn, name, team):
        cmd="INSERT INTO coaches VALUES ('"+ssn+"', '"+name+"', '"+team+"')"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def insertcontract(self, ssn, value, length):
        cmd="INSERT INTO contracts VALUES ('"+ssn+"', "+value+", "+length+")"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def insertschool(self, name, location, ranking):
        cmd="INSERT INTO schools VALUES ('"+name+"', '"+location+"', "+ranking+")"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def delete(self, key, value,table):
        cmd="DELETE FROM "+table+" WHERE "+key+"='"+value+"'"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def update(self, ssn, name, team, school):
        cmd="UPDATE players SET name='"+name+"', team='"+team+"', school='"+school+"' WHERE SSN='"+ssn+"'"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def cmd(self, cmd):
        cmd=cmd
        self.cursor.execute(cmd)
        return self.cursor.fetchall()
        
        
    def deleteall(self):
        cmd="DELETE FROM players"
        self.cursor.execute(cmd)
        self.connection.commit()
        cmd="DELETE FROM teams"
        self.cursor.execute(cmd)
        self.connection.commit()
        cmd="DELETE FROM coaches"
        self.cursor.execute(cmd)
        self.connection.commit()
        cmd="DELETE FROM contracts"
        self.cursor.execute(cmd)
        self.connection.commit()
        cmd="DELETE FROM schools"
        self.cursor.execute(cmd)
        self.connection.commit()
    

    def __del__(self):
        self.connection.close()


'''
db=Datebase('project.db')
#db.insertteam(name='111',city='222',arena='333',owner='444')
db.delete('name','aaa','teams')
db.update('aac','c','a','d')
print("Teams")
print(db.fetch('teams'))
print("Players")
print(db.fetch('players'))
print("Coaches")
print(db.fetch('coaches'))
print("Contracts")
print(db.fetch('contracts'))
print("Schools")
print(db.fetch('schools'))
'''