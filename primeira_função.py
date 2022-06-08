


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


