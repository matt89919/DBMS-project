import tkinter as TK
from db import Datebase

db=Datebase('project.db')

def populate(table):
    return

app = TK.Tk()
app.title('DBMS project')
app.geometry('700x700')

# player blanks
player = TK.StringVar()
playerlabel = TK.Label(app, text="Player name", font=('bold',14), pady=20)
playerlabel.grid(row=0, column=0, sticky=TK.W)

playerentry = TK.Entry(app, textvariable=player)
playerentry.grid(row=1, column=0)

pteam = TK.StringVar()
pteamlabel = TK.Label(app, text="Player team", font=('bold',14))
pteamlabel.grid(row=2, column=0, sticky=TK.W)

pteamentry = TK.Entry(app, textvariable=pteam)
pteamentry.grid(row=3, column=0)



app.mainloop()