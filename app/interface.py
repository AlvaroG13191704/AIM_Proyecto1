from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.geometry("535x435")
root.resizable(False, False)
root.title("Login")

# Función para realizar el login
def login():
    username = "admin"
    password = "password123"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Success", message="Access granted.")
    else:
        messagebox.showerror(title="Error", message="Access denied.")

# Cargando la imagen de fondo
img_path = os.path.join(os.path.dirname(__file__), "images/login.png")
bg_img = PhotoImage(file=img_path)

# Creando el canvas
canvas = Canvas(root, width=540, height=440, bg="#FFFFFF")
canvas.pack()

# Colocando la imagen de fondo en el canvas
canvas.create_image(0, 0, image=bg_img, anchor=NW)

# Creando los widgets
username_entry = Entry(root, font=("Arial", 16), bg="#FFFFFF")
username_entry.place(x=190, y=150)

password_entry = Entry(root, show="*", font=("Arial", 16), bg="#FFFFFF")
password_entry.place(x=190, y=185)

login_button = Button(root, text="Ingresar", font=("Arial", 16), bg="#49B8A9", fg="#FFFFFF", width=10, command=login)
login_button.place(x=200, y=270)

root.mainloop()