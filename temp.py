'''
import tkinter

aluno = tkinter.Tk()
aluno.title("Senac")
aluno.mainloop()



teste




















-------------------------------

from tkinter import Tk

window = Tk()
window.title('SENAC')
window.geometry("500x300")
#window.iconbitmap('app.ico')
window.resizable(False, False)
window.mainloop()


























-------------------------------------------------------


from tkinter import Tk, Button, Label, Entry, Listbox
from tkinter import MULTIPLE

window = Tk()
window.title('Title')
window.geometry("500x300")
#window.geometry("500x500+200+200")
#window.maxsize(700,700)
#window.state("zoomed")
#window.state("iconic")
window.iconbitmap('mario.ico')
window['bg'] = 'blue'
window.resizable(True, True)

#elements
btn1 = Button(window, text = "Clique Aqui")
btn1.place(x = 50, y = 50)

lbi1 = Label(window, text = "Seu nome")
lbi1.place(x = 100, y = 100)
ent1 = Entry(window, width = 20)
ent1.place(x = 200, y = 100)

lstbox = Listbox(window, selectmode=MULTIPLE)
lstbox.insert(1,"Python")
lstbox.insert(2,"C")
lstbox.insert(3,"PHP")
lstbox.insert(4,"HTML")
lstbox.place(x = 200, y = 200)

window.mainloop()












from tkinter import messagebox, Tk, Button

def btn1_func():
    messagebox.askyesno("Hello Mundo", "Olá eu trabalho para o Esdras")
    window = Tk()
    window.geometry("500x300")
    window['bg'] = 'black'
    window.state("zoomed")
    window.iconbitmap('mario.ico')
    window.mainloop()

window = Tk()
window.title('Minha primeira função')
window.geometry("900x800")
window.resizable(True, True)

btn1 = Button(window, text = "Aqui", command = btn1_func)
btn1.place(x = 50, y = 50)

window.mainloop()



















from tkinter import Tk, Menu

def pare():
    window.destroy()

window = Tk()
window.title('Minha segunda função')
window.geometry("900x800")
#window.iconbitmap('mario.ico')
window.resizable(True, True)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label = 'Sair', command = pare)

menu.add_cascade(label = 'File' , menu = new_item)
window.config(menu = menu)

window.mainloop()


























from tkinter import *
root =Tk()
class App():
    def __init__(self):
        self.root = root
        self.config()
        self.calculadora()
        root.mainloop()
    def config(self):
        self.root.title("Calculadora muito simples")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
    def calculadora(self):
        self.lbl1 = Label(text='Primeiro número: ')
        self.lbl1.place(relx=0.15,rely=0.1)
        self.numero1 = DoubleVar()
        self.lbl1_enty = Entry(textvariable=self.numero1)
        self.lbl1_enty.place(relx=0.45,rely=0.1)
        self.lbl2 = Label(text='Segundo número: ')
        self.lbl2.place(relx=0.15, rely=0.25)
        self.numero2 = DoubleVar()
        self.lbl2_enty = Entry(textvariable=self.numero2)
        self.lbl2_enty.place(relx=0.45, rely=0.25)
      # Resultado
        self.lbl3 = Label(text='Resultado')
        self.lbl3.place(relx=0.3, rely=0.7)
        self.resultado = StringVar()
        self.l_resultado = Label(textvariable=self.resultado, font=("Helvetica", '8'))
        self.l_resultado.place(relx=0.5, rely=0.7)

       #Butão
        self.btn1 = Button(text='Soma',command=self.soma)
        self.btn1.place(relx=0.15, rely=0.45)
        self.btn2 = Button(text='Subtração',command=self.sub)
        self.btn2.place(relx=0.3, rely=0.45)
        self.btn3 = Button(text='Divisão',command=self.div)
        self.btn3.place(relx=0.5, rely=0.45)
        self.btn4 = Button(text='Multiplicação',command=self.mult)
        self.btn4.place(relx=0.65, rely=0.45)

    def soma(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = num1 + num2
        self.resultado.set(resul)
    def sub(self):
      num1 = self.numero1.get()
      num2 = self.numero2.get()
      resul = num1 - num2
      self.resultado.set(resul)
    def mult(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = num1 * num2
        self.resultado.set(resul)
    def div(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = round((num1 / num2),2)
        self.resultado.set(resul)
        
App()








from tkinter import *
import tkinter.font as font 
  
  
  
root = Tk() 
root.geometry("380x400") 
root.title("Calculator") 
root.resizable(0, 0) 
inp = StringVar() 
myFont = font.Font(size=15) 
  
screen = Entry(root, text=inp, width=30,  
               justify='right', font=(10), bd=4) 
screen.grid(row=0, columnspan=4, padx=15, 
            pady=15, ipady=5) 
key_matrix = [["c", u"\u221A", "/", "<-"],  
              ["7", "8", "9", "*"], 
              ["4", "5", "6", "-"],  
              ["1", "2", "3", "+"], 
              ["!", 0, ".", "="]] 
btn_dict = {} 
ans_to_print = 0
def Calculate(event): 
    
    
button = event.widget.cget("text") 
  
    
    global key_matrix, inp, ans_to_print 
  
    try:
        if button == u"\u221A": 
            ans = float(inp.get())**(0.5) 
            ans_to_print = str(ans) 
            inp.set(str(ans)) 
        elif button == "c":  
                    inp.set("") 
        elif button == "!":  
                    def fact(n): return 1 if n == 0 else n*fact(n-1) 
                    inp.set(str(fact(int(inp.get())))) 
        elif button == "<-":  
                    inp.set(inp.get()[:len(inp.get())-1]) 
        elif button == "=":  
                      ans_to_print = str(eval(inp.get())) 
                    inp.set(ans_to_print) 
        else: 
                      inp.set(inp.get()+str(button)) 
          
            except: 
              inp.set("Wrong Operation") 
  
  
  
for i in range(len(key_matrix)):   
    
    for j in range(len(key_matrix[i])):   
        btn_dict["btn_"+str(key_matrix[i][j])] = Button( 
          root, bd=1, text=str(key_matrix[i][j]), font=myFont) 
        
        btn_dict["btn_"+str(key_matrix[i][j])].grid( 
          row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5) 
        
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate) 

root.mainloop()














import sqlite3
# conectando
bd = sqlite3.connect('nome.db')
# definindo um cursor
cursor = bd.cursor()
# criando a tabela (shema)
cursor.execute("CREATE TABLE employees (id integer PRIMARI KEY, name text, salary real, department text, position text, hiredate text)")

cursor.execute("INSERT INTO employees (id, name, salary, department, position, hiredate)VALUES(1, 'Esdras', 988, 'HR', 'Gerente', '2022-02-4')")
bd.commit()








import sqlite3

conn = sqlite3.connect('clientes2.db')

cursor = conn.cursor()

#cursor.execute("CREATE TABLE clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER, cpf VARCHAR(11) NOT NULL, email TEXT NOT NULL, fone VARCHAR(11) NOT NULL, cidade TEXT, uf VARCHAR(2) NOT NULL, criado_em DATE NOT NULL)")

#print('Tabela criada com sucesso')

cursor.execute ("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em) VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11987654321', 'Sao Paulo', 'SP', '2014-06-08')")

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '98765-4322', 'Porto Alegre', 'RS', '2014-06-09')")

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES ('Bruna', 21, '22222222222', 'bruna@email.com', '21-98765-4323', 'Rio de Janeiro', 'RJ', '2014-06-09')")

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES ('Matheus', 19, '33333333333', 'matheus@email.com', '11-98765-4324', 'Campinas', 'SP', '2014-06-08')")

conn.commit()

print('Dados inseridos com sucesso.')
#desconectando
conn.close()









# 04_create_data_nrecords.py
import sqlite3

conn = sqlite3.connect('clientes2.db')
cursor = conn.cursor()

# criando uma lista de dados
lista = [('Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2014-06-09'),('Joao', 21, '55555555555', 'joao@email.com','11-1234-5600', 'Sao Paulo', 'SP', '2014-06-09'),('Xavier', 24, '66666666666', 'xavier@email.com', '12-1234-5601', 'Campinas', 'SP', '2014-06-10')]

# inserindo dados na tabela
cursor.executemany("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES (?,?,?,?,?,?,?,?)", lista)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()








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
            





import tkinter as tk


def criarnovajanela():
    novajanela = tk.Toplevel(app)

app = tk.Tk()
botao = tk.Button(app, text = "Criar janela", command = criarnovajanela)
#app.state("zoomed")
app.geometry('500x600')
botao.pack()

app.mainloop()





import qrcode

image_qrcode = qrcode.make("https://www.google.com/")
image_qrcode.save("qrcode_python.jpg")





import qrcode
links_produtos = {"produto1": "123456", "produto2": "123456", "produto3": "123456", "produto4": "123456"}

for produto in links_produtos:
    #print(produto)
    #print(links_produtos[produto])
    link = links_produtos[produto]
    image_qrcode = qrcode.make(link)
    image_qrcode.save(f"qrcode_(produto).jpg")

'''


import qrcode
links_produtos = {"produto1": "123456", "produto2": "123456", "produto3": "123456", "produto4": "123456"}

for produto in links_produtos:
    #print(produto)
    #print(links_produtos[produto])
    link = links_produtos[produto]
    image_qrcode = qrcode.make(link)
    image_qrcode.save(f"qrcode_(produto).jpg")



