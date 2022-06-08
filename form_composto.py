

from tkinter import * 
import sqlite3

root = Tk()
root.geometry('500x600')
root.title('Formulário')

fullname = StringVar()
email = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()


def database():
    nome = fullname.get()
    email = Email.get()
    gender = var.get()
    country = c.get()
    prog = var1.get()
    conn = sqlite3.connect('form2.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS student (fullname TEXT)')
    cursor.execute('INSERT INTO student (fullname) VALUES(?)',(nome,))
    conn.commit()
###############################################################################
label_0 = Label(root, text = 'Fomulário', width = 20, font = ('bold', 20))
label_0.place(x = 90, y = 53)

label_1 = Label(root, text = 'Nome', width = 20, font = ('bold', 10))
label_1.place(x = 80, y = 130)

entry_1 = Entry(root, textvar = fullname)
entry_1.place(x = 240, y = 130)

label_2 = Label(root, text = 'Email', width = 20, font = ('bold', 10))
label_2.place(x = 68, y = 180)

entry_2 = Entry(root, textvar = email)
entry_2.place(x = 240, y = 180)

label_3 = Label(root, text = 'Gênero', width = 20, font = ('bold', 10))
label_3.place(x = 70, y = 230)

Radiobutton(root, text = 'Male', padx = 5, variable = var, value = 1).place(x = 235, y = 230)
Radiobutton(root, text = 'Female', padx = 20, variable = var, value = 2).place(x = 300, y = 230)

label_4 = Label(root, text = 'Country', width = 20, font = ('bold', 10))
label_4.place(x = 70, y = 280)

list1 = {'Philippines', 'Japan', 'Korea', 'China', 'Singapore', 'Hong kong'};

droplist = OptionMenu(root, c, *list1)
droplist.config(width = 15)
c.set('select your country')
droplist.place(x = 240, y = 280)

label_5 = Label(root, text = 'Pogramming', width = 20, font = ('bold', 10))
label_5.place(x = 85, y = 330)
var2 = IntVar()

Checkbutton(root, text = 'java', variable = var1).place(x = 235, y = 330)
Checkbutton(root, text = 'Python', variable = var2).place(x = 290, y = 330)
###############################################################################
Button(root, text = 'Entrar', width = 20, bg = 'brown',fg = 'white', command = database).place(x = 180, y = 380)
            
root.mainloop()
            

