import tkinter as TK
from tkinter import END, Entry, messagebox
from typing import List
from unittest import result

from matplotlib.colors import cnames
from db import Datebase

db=Datebase('project.db')


def populate():
    partlist.delete(0,TK.END)
    clist.delete(0,TK.END)
    colist.delete(0,TK.END)
    slist.delete(0,TK.END)
    tlist.delete(0,TK.END)
    for row in db.fetch('players'):
        partlist.insert(TK.END, row)
    for row in db.fetch('coaches'):
        clist.insert(TK.END, row)
    for row in db.fetch('contracts'):
        colist.insert(TK.END, row)
    for row in db.fetch('schools'):
        slist.insert(TK.END, row)
    for row in db.fetch('teams'):
        tlist.insert(TK.END, row)

def insertp():
    pn=player.get()
    ps=pssn.get()
    psc=pschool.get()
    pt=pteam.get()
    if pn=='' or psc=='' or ps=='' or pt=='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    
    db.insertplayer(ps, pn, pt, psc)
    clear_text()
    populate()

def insertc():
    cs=cssn.get()
    cn=coach.get()
    ct=cteam.get()
    if cn=='' or cs=='' or ct=='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    
    db.insertcoach(cs, cn, ct)
    clear_text()
    populate()

def insertt():
    tn=tname.get()
    tl=tlocation.get()
    ta=tarena.get()
    to=towner.get()
    if tn=='' or tl=='' or ta=='' or to=='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    
    db.insertteam(tn, tl, ta, to)
    clear_text()
    populate()

def insertcontract():
    cos=cossn.get()
    cl=clength.get()
    cv=cvalue.get()
    if cos=='' or cl=='' or cv=='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    
    if cl.isdigit() and cv.isdigit():
        db.insertcontract(cos, cl, cv)
        clear_text()
        populate()
    else:
        messagebox.showerror('Required INT', 'Please input a INT to Length and Value')
        return
    
def insertr():
    sn=sname.get()
    sl=slocation.get()
    sr=ranking.get()
    if sn=='' or sl=='' or sr=='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    
    if sr.isdigit():
        db.insertschool(sn, sl, sr)
        clear_text()
        populate()
    else:
        messagebox.showerror('Required INT', 'Please input a INT to NCAA Ranking')
        return
    
def clear_text():
    playerentry.delete(0,END)
    pssnentry.delete(0,END)
    pschoolentry.delete(0,END)
    pteamentry.delete(0,END)
    centry.delete(0,END)
    cssnentry.delete(0,END)
    cteamentry.delete(0,END)
    tnameentry.delete(0,END)
    taentry.delete(0,END)
    tlentry.delete(0,END)
    clentry.delete(0,END)
    cossnentry.delete(0,END)
    cventry.delete(0,END)
    cssnentry.delete(0,END)
    snentry.delete(0,END)
    slentry.delete(0,END)
    rentry.delete(0,END)
    sqlentry.delete("1.0",END)
    
def query():
    cmd=sqlentry.get("1.0","end-1c")
    print(cmd)
    try:
        resultbox.delete(0,END)
        resultbox.insert(TK.END, cmd)
        resultbox.insert(TK.END, "\n")
        for row in db.cmd(cmd):
            resultbox.insert(TK.END, row)
    except:
        resultbox.insert(TK.END, "BAD QUERY, check your syntax")
        return
    clear_text()
    populate()   

app = TK.Tk()
app.title('DBMS project')
app.geometry('930x700')

# player blanks
pssn = TK.StringVar()
pssnlabel = TK.Label(app, text="Player's SSN", font=('bold',14))
pssnlabel.grid(row=0, column=0, padx=20, pady=5)

pssnentry = TK.Entry(app, textvariable=pssn)
pssnentry.grid(row=1, column=0, padx=20, pady=5)

player = TK.StringVar()
playerlabel = TK.Label(app, text="Player's name", font=('bold',14))
playerlabel.grid(row=2, column=0, padx=20, pady=5)

playerentry = TK.Entry(app, textvariable=player)
playerentry.grid(row=3, column=0, padx=20, pady=5)

pteam = TK.StringVar()
pteamlabel = TK.Label(app, text="Player's team", font=('bold',14))
pteamlabel.grid(row=4, column=0, padx=20, pady=5)

pteamentry = TK.Entry(app, textvariable=pteam)
pteamentry.grid(row=5, column=0, padx=20, pady=5)

pschool = TK.StringVar()
pschoollabel = TK.Label(app, text="Player's school", font=('bold',14))
pschoollabel.grid(row=6, column=0, padx=20, pady=5)

pschoolentry = TK.Entry(app, textvariable=pschool)
pschoolentry.grid(row=7, column=0, padx=20, pady=5)

insertp = TK.Button(app, text="Insert new player", width=18, command=insertp)
insertp.grid(row=8, column=0, padx=20, pady=20)

partlist = TK.Listbox(app, height=10, width=20, border=0)
partlist.grid(row=9, column=0, padx=20, pady=10)

# coach blanks
cssn = TK.StringVar()
cssnlabel = TK.Label(app, text="Coach's SSN", font=('bold',14))
cssnlabel.grid(row=0, column=1, padx=20, pady=5)

cssnentry = TK.Entry(app, textvariable=cssn)
cssnentry.grid(row=1, column=1, padx=20, pady=5)

coach = TK.StringVar()
clabel = TK.Label(app, text="Coach's name", font=('bold',14))
clabel.grid(row=2, column=1, padx=20, pady=5)

centry = TK.Entry(app, textvariable=coach)
centry.grid(row=3, column=1, padx=20, pady=5)

cteam = TK.StringVar()
cteamlabel = TK.Label(app, text="Coach's team", font=('bold',14))
cteamlabel.grid(row=4, column=1, padx=20, pady=5)

cteamentry = TK.Entry(app, textvariable=cteam)
cteamentry.grid(row=5, column=1, padx=20, pady=5)

insertc = TK.Button(app, text="Insert new coach", width=18, command=insertc)
insertc.grid(row=8, column=1, padx=20, pady=20)

clist = TK.Listbox(app, height=10, width=20, border=0)
clist.grid(row=9, column=1, padx=20, pady=10)

# team blank
tname = TK.StringVar()
tnamelabel = TK.Label(app, text="Team's name", font=('bold',14))
tnamelabel.grid(row=0, column=2, padx=20, pady=5)

tnameentry = TK.Entry(app, textvariable=tname)
tnameentry.grid(row=1, column=2, padx=20, pady=5)

tlocation = TK.StringVar()
tlabel = TK.Label(app, text="Team's location", font=('bold',14))
tlabel.grid(row=2, column=2, padx=20, pady=5)

tlentry = TK.Entry(app, textvariable=tlocation)
tlentry.grid(row=3, column=2, padx=20, pady=5)

tarena = TK.StringVar()
talabel = TK.Label(app, text="Team's arena", font=('bold',14))
talabel.grid(row=4, column=2, padx=20, pady=5)

taentry = TK.Entry(app, textvariable=tarena)
taentry.grid(row=5, column=2, padx=20, pady=5)

towner = TK.StringVar()
tolabel = TK.Label(app, text="Team's owner", font=('bold',14))
tolabel.grid(row=6, column=2, padx=20, pady=5)

toentry = TK.Entry(app, textvariable=towner)
toentry.grid(row=7, column=2, padx=20, pady=5)

insertt = TK.Button(app, text="Insert new team", width=18, command=insertt)
insertt.grid(row=8, column=2, padx=20, pady=20)

tlist = TK.Listbox(app, height=10, width=20, border=0)
tlist.grid(row=9, column=2, padx=20, pady=5)

# contract blank
cossn = TK.StringVar()
cossnlabel = TK.Label(app, text="Player's SSN", font=('bold',14))
cossnlabel.grid(row=0, column=3, padx=20, pady=5)

cossnentry = TK.Entry(app, textvariable=cossn)
cossnentry.grid(row=1, column=3, padx=20, pady=5)

cvalue = TK.StringVar()
cvlabel = TK.Label(app, text="Contract value", font=('bold',14))
cvlabel.grid(row=2, column=3, padx=20, pady=5)

cventry = TK.Entry(app, textvariable=cvalue)
cventry.grid(row=3, column=3, padx=20, pady=5)

clength = TK.StringVar()
cllabel = TK.Label(app, text="Contract length", font=('bold',14))
cllabel.grid(row=4, column=3, padx=20, pady=5)

clentry = TK.Entry(app, textvariable=clength)
clentry.grid(row=5, column=3, padx=20, pady=5)

insertcontract = TK.Button(app, text="Insert new contract", width=18, command=insertcontract)
insertcontract.grid(row=8, column=3, padx=20, pady=20)

colist = TK.Listbox(app, height=10, width=20, border=0)
colist.grid(row=9, column=3, padx=20, pady=10)

# school blank
sname = TK.StringVar()
snlabel = TK.Label(app, text="School's name", font=('bold',14))
snlabel.grid(row=0, column=4, padx=20, pady=5)

snentry = TK.Entry(app, textvariable=sname)
snentry.grid(row=1, column=4, padx=20, pady=5)

slocation = TK.StringVar()
sllabel = TK.Label(app, text="School's location", font=('bold',14))
sllabel.grid(row=2, column=4, padx=20, pady=5)

slentry = TK.Entry(app, textvariable=slocation)
slentry.grid(row=3, column=4, padx=20, pady=5)

ranking = TK.StringVar()
rlabel = TK.Label(app, text="NCAA ranking", font=('bold',14))
rlabel.grid(row=4, column=4, padx=20, pady=5)

rentry = TK.Entry(app, textvariable=ranking)
rentry.grid(row=5, column=4, padx=20, pady=5)

insertr = TK.Button(app, text="Insert new school", width=18, command=insertr)
insertr.grid(row=8, column=4, padx=20, pady=10)

slist = TK.Listbox(app, height=10, width=20, border=0)
slist.grid(row=9, column=4, padx=20, pady=10)


# text box
sqlentry = TK.Text(app, height=5, width=20)
sqlentry.grid(row=10, column=2, padx=20, pady=10, columnspan=1)

query = TK.Button(app, text="Query by SQLite", width=18, command=query)
query.grid(row=11, column=2, padx=20, pady=5)

# result box
resultbox = TK.Listbox(app, height=10, width=30, border=0)
resultbox.grid(row=10, column=3, padx=20, pady=10, columnspan=2, rowspan=2)

populate()
app.mainloop()