from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# Función para realizar el login
def login():
    username = "admin"
    password = "123"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login", message="Bienvenido "+username)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        # Ocultar la ventana de inicio de sesión    
        root.withdraw()
        # Abrir la ventana principal
        open_main_window()
    else:
        messagebox.showerror(title="Error", message="Acceso denegado")

def open_main_window():
    # Crear la ventana principal
    main_window = tk.Toplevel()
    main_window.title("Ventana Principal")
    main_window.resizable(False, False)
    main_window.geometry("840x440")
    main_window.protocol("WM_DELETE_WINDOW", show_login)  # Volver al login al cerrar

    def close_main_window():
        main_window.withdraw()
        show_login()

    def configure():
        configure_window = tk.Toplevel()
        configure_window.title("configure")
        configure_window.resizable(False, False)
        configure_window.geometry("640x440")

        def aceptar():
            type = selected_option1.get()
            encrypt_log = selected_option2.get()
            encrypt_read = selected_option3.get()
            llave = text_entry.get()

            print("Tipo:", type)
            print("Valor1:", encrypt_log)
            print("Valor2:", encrypt_read)
            print("Texto:", llave)

            configure_window.withdraw()

        # Cargando la imagen de fondo de la ventana configure
        img_path2 = os.path.join(os.path.dirname(__file__), "images/configure.png")
        bg_img2 = Image.open(img_path2)
        image2 = ImageTk.PhotoImage(bg_img2)

        # Creando el canvas
        canvas2 = Canvas(configure_window, width=640, height=440)
        canvas2.pack()

        # Colocando la imagen de fondo en el canvas
        canvas2.create_image(0, 0, image=image2, anchor=NW)
        canvas2.image = image2  # Haz referencia a la imagen para evitar que esta se borre por el Garbage Collector

        # widgets de la ventana configure
        optionsTYPE = ["Local", "Cloud"]
        optionsTF = [True, False]
        selected_option1 = tk.StringVar()
        selected_option2 = tk.StringVar()
        selected_option3 = tk.StringVar()
        text_entry = tk.StringVar()

        combo1 = ttk.Combobox(configure_window, width=40, font=("Arial", 12), values=optionsTYPE, state="readonly", textvariable=selected_option1)
        combo1.place(x=200, y=95)
        combo2 = ttk.Combobox(configure_window, width=40, font=("Arial", 12), values=optionsTF, state="readonly", textvariable=selected_option2)
        combo2.place(x=200, y=160)
        combo3 = ttk.Combobox(configure_window, width=40, font=("Arial", 12), values=optionsTF, state="readonly", textvariable=selected_option3)
        combo3.place(x=200, y=225)
        entry = Entry(configure_window, font=("Arial", 12), width=40, textvariable=text_entry)
        entry.place(x=200, y=290)
        aceptar_button = Button(configure_window, text="Aceptar", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=10, command=aceptar)
        aceptar_button.place(x=250, y=370)

        

    def transfer():
        transfer_window = tk.Toplevel()
        transfer_window.title("transfer")
        transfer_window.resizable(False, False)
        transfer_window.geometry("640x440")

        def aceptar():
            type = selected_option1.get()
            encrypt_log = selected_option2.get()
            encrypt_read = selected_option3.get()
            llave = text_entry.get()

            print("Tipo:", type)
            print("Valor1:", encrypt_log)
            print("Valor2:", encrypt_read)
            print("Texto:", llave)

            transfer_window.withdraw()

        # Cargando la imagen de fondo de la ventana transfer
        img_path2 = os.path.join(os.path.dirname(__file__), "images/transfer.png")
        bg_img2 = Image.open(img_path2)
        image2 = ImageTk.PhotoImage(bg_img2)

        # Creando el canvas
        canvas2 = Canvas(transfer_window, width=640, height=440)
        canvas2.pack()

        # Colocando la imagen de fondo en el canvas
        canvas2.create_image(0, 0, image=image2, anchor=NW)
        canvas2.image = image2  # Haz referencia a la imagen para evitar que esta se borre por el Garbage Collector

        # widgets de la ventana transfer
        optionsTYPE = ["Local", "Cloud"]
        optionsTF = [True, False]
        selected_option1 = tk.StringVar()
        selected_option2 = tk.StringVar()
        selected_option3 = tk.StringVar()
        text_entry = tk.StringVar()

        combo1 = ttk.Combobox(transfer_window, width=40, font=("Arial", 12), values=optionsTYPE, state="readonly", textvariable=selected_option1)
        combo1.place(x=200, y=95)
        combo2 = ttk.Combobox(transfer_window, width=40, font=("Arial", 12), values=optionsTF, state="readonly", textvariable=selected_option2)
        combo2.place(x=200, y=160)
        combo3 = ttk.Combobox(transfer_window, width=40, font=("Arial", 12), values=optionsTF, state="readonly", textvariable=selected_option3)
        combo3.place(x=200, y=225)
        entry = Entry(transfer_window, font=("Arial", 12), width=40, textvariable=text_entry)
        entry.place(x=200, y=290)
        aceptar_button = Button(transfer_window, text="Aceptar", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=10, command=aceptar)
        aceptar_button.place(x=250, y=370)

    def create():
        # Crear la ventana de creación
        pass

    def rename():
        # Crear la ventana de renombrar
        pass

    def delete():
        # Crear la ventana de eliminar
        pass

    def modify():
        # Crear la ventana de modificar
        pass

    def copy():
        # Crear la ventana de copiar
        pass

    def add():
        # Crear la ventana de agregar
        pass

    def backup():
        # Crear la ventana de respaldo
        pass

    def execu():
        # Crear la ventana de ejecutar
        pass


    main_window.protocol("WM_DELETE_WINDOW", close_main_window)

    # Cargando la imagen de fondo de la ventana principal
    img_path = os.path.join(os.path.dirname(__file__), "images/ventanaprincipal.png")
    bg_img = Image.open(img_path)
    image = ImageTk.PhotoImage(bg_img)

    # Creando el canvas
    canvas = Canvas(main_window, width=840, height=440)
    canvas.pack()

    # Colocando la imagen de fondo en el canvas
    canvas.create_image(0, 0, image=image, anchor=NW)
    canvas.image = image  # Haz referencia a la imagen para evitar que esta se borre por el Garbage Collector


    espaciado=35
    # Contenido de la ventana principal
    configure_b = Button(main_window, text="configure", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=configure)
    configure_b.place(x=500, y=90)

    transfer_b= Button(main_window, text="transfer", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=transfer)
    transfer_b.place(x=650, y=90)

    create_b = Button(main_window, text="create", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=create)
    create_b.place(x=500, y=110+espaciado)

    rename_b= Button(main_window, text="rename", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=rename)
    rename_b.place(x=650, y=110+espaciado)

    delete_b= Button(main_window, text="delete", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=delete)
    delete_b.place(x=500, y=130+espaciado*2)

    modify_b= Button(main_window, text="modify", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=modify)
    modify_b.place(x=650, y=130+espaciado*2)

    copy_b= Button(main_window, text="copy", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=copy)
    copy_b.place(x=500, y=150+ espaciado*3)

    add_b = Button(main_window, text="add", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=add)
    add_b.place(x=650, y=150+espaciado*3)

    backup_b= Button(main_window, text="backup", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=backup)
    backup_b.place(x=500, y=170+espaciado*4)

    execu_b= Button(main_window, text="execu", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=execu)
    execu_b.place(x=650, y=170+espaciado*4)

    cerrars_b= Button(main_window, text="Cerrar Sesión", font=("Arial", 12), bg="#49B8A9", fg="#FFFFFF", width=12, command=close_main_window)
    cerrars_b.place(x=500, y=190+espaciado*5)

    console_txt = Text(main_window, width=45, height=18, font=("Arial", 12))
    console_txt.place(x=40, y=90)


def show_login():
    # Mostrar la ventana de inicio de sesión
    root.deiconify()


root = Tk()
root.geometry("540x440")
root.resizable(False, False)
root.title("Login")

# Cargando la imagen de fondo de la ventana de inicio de sesión
img_path = os.path.join(os.path.dirname(__file__), "images/login.png")
bg_img = Image.open(img_path)
image = ImageTk.PhotoImage(bg_img)

# Creando el canvas
canvas = Canvas(root, width=540, height=440, bg="#FFFFFF")
canvas.pack()

# Colocando la imagen de fondo en el canvas
canvas.create_image(0, 0, image=image, anchor=NW)
canvas.image = image  # Haz referencia a la imagen para evitar que esta se borre por el Garbage Collector

# Creando los widgets
username_entry = Entry(root, font=("Arial", 12), bg="#FFFFFF", width=20)
username_entry.place(x=190, y=150)

password_entry = Entry(root, show="*", font=("Arial", 12), bg="#FFFFFF", width=20)
password_entry.place(x=190, y=185)

login_button = Button(root, text="Ingresar", font=("Arial", 14), bg="#49B8A9", fg="#FFFFFF", width=10, command=login)
login_button.place(x=200, y=270)

# Cerrar la ventana principal al hacer clic en la "X"
root.protocol("WM_DELETE_WINDOW", root.quit)

root.mainloop()