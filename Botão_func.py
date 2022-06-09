
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

