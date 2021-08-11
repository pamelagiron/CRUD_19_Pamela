from tkinter import *
from tkinter import ttk
import database

#print('DATA (FrontEnd): ' + str(database.data))

def mostrar_usuarios():
    registro = 0
    for fila in database.data:
        registro = registro + 1 
        print('DATA (FrontEnd): ' + str(registro) +" - "+ str(fila))
        nombre = fila[0]  
        correo = fila[1]
        telefono = fila[2]  
        my_table.insert(parent='', index='end', iid=registro, text=str(registro), 
            values=(nombre, correo, telefono))



def insertar_usuario():
    # Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
  
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    demo_db = database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    demo_db.insert_db(nombre, correo, telefono)
    demo_db.read_db()
    mostrar_usuarios()
    


window = Tk()
frame_app = Frame(window, width=400, height=400, bg="#e6b68b")
frame_app.pack()

my_table = ttk.Treeview(frame_app)

# Define Our Columns 
my_table['columns'] = ('NOMBRE', 'CORREO', 'TELEFONO')

# Formate Our Columns
my_table.column('#0', width=120, minwidth=50)
my_table.column('NOMBRE', anchor=W, width=120)
my_table.column('CORREO', anchor=W, width=120)
my_table.column('TELEFONO', anchor=W, width=120)

# Create Headings
my_table.heading('#0', text='ID_CLIENTE', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
my_table.heading('CORREO', text='CORREO', anchor=W)
my_table.heading('TELEFONO', text='TELEFONO', anchor=W)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=50, bg="#cd966c")
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=90, bg="#cd966c")
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=350, bg="#cd966c")
frame_options.grid(row=2, column=0)
my_table.grid(row=3, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="TIENDA SADASHI",
              font=("Century Gothic", "14",))
title.place(x=150, y=20)

# Widgets dentro del contender TITLE

title2 = Label(frame_title, 
              text="ESPERO ENCUENTRES LO QUE BUSCAS.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)

# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=350, bg="#cd966c")
frame_form.place(x=25, y=5)
label_nombre = Label(frame_form, 
              text="NOMBRE:",
              font=("Century Gothic", "14", "bold"),
              fg="white",
              bg="#cd966c")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=70)

label_correo = Label(frame_form, 
              text="CORREO:",
              font=("Century Gothic", "14", "bold"),
              fg="white",
              bg="#cd966c")
label_correo.place(x=30, y=100)
entry_correo = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_correo.place(x=30, y=140)

label_telefono = Label(frame_form, 
              text="TELEFONO:",
              font=("Century Gothic", "14", "bold"),
              fg="white",
              bg="#cd966c")
label_telefono.place(x=30, y=170)
entry_telefono = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_telefono.place(x=30, y=200)


button_agregar = Button(frame_form, text="Insertar usuario", 
                        font=("Century Gothic", "14", "bold"),
                        command=insertar_usuario)
button_agregar.place(x=110, y=250)

window.mainloop()