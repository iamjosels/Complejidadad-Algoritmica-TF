from pathlib import Path

#from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import os
import subprocess

def windows_login_w():
    #Assets
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\josel\OneDrive\Escritorio\Visual Code\Interfaz Tkinter\project\Login\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    global window_main

    #VALIDAR LOGIN
    def login():
        email = email_user.get()
        password = password_user.get()
        
        # Leer los datos de registro desde el archivo de texto
        with open("registro.txt", "r") as file:
            data = file.read().splitlines()
        
        if len(data) == 0:
            messagebox.showinfo("Usuario no reconocido", "No hay usuarios registrados. Por favor, regístrese.")
            window_login.destroy()
            window_register()
        else:
            saved_email = data[0]
            saved_username = data[1]
            saved_password = data[2]
            
            if (email == saved_email or email == saved_username) and password == saved_password:
                messagebox.showinfo("Inicio de Sesión Exitoso", "¡Has iniciado sesión correctamente!")
                window_login.destroy()
                subprocess.call(["python", os.path.join("TrabajoFinal\\Main.py")])
                #window_main_w()
            else:
                messagebox.showerror("Error de Inicio de Sesión", "Las credenciales son incorrectas.")

                
    #REGISTRO
    def window_register():
        window_register = Tk()
        window_register.geometry("662x444")
        window_register.configure(bg="#F0F8F8")

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\josel\OneDrive\Escritorio\Visual Code\Interfaz Tkinter\project\Register\build\assets\frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def register():
            email = entry_email.get()
            username = entry_user.get()
            password = entry_password.get()
            
            # Guardar los datos en un archivo de texto
            with open("registro.txt", "r") as file:
                data = file.read().splitlines()
                
            saved_email = ""
            saved_username = "" 
            
            if len(data) > 0:
                saved_email = data[0]
                saved_username = data[1]

            if email == saved_email or username == saved_username:
                messagebox.showerror("Error de Registro", "El Email o Username ya están en uso.")
            
            else:
                # Guardar los datos de registro en el archivo de texto
                with open("registro.txt", "w") as file:
                    file.write(email + "\n")
                    file.write(username + "\n")
                    file.write(password + "\n")

                messagebox.showinfo("Registro Exitoso", "El usuario se ha registrado exitosamente.")
                window_register.destroy()
                windows_login_w()
                
                        
        canvas = Canvas(
            window_register,
            bg = "#F0F8F8",
            height = 444,
            width = 662,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            393.0,
            167.0,
            anchor="nw",
            text="Email",
            fill="#828282",
            font=("NunitoSans SemiBold", 10 * -1)
        )

        canvas.create_text(
            393.0,
            276.0,
            anchor="nw",
            text="Password",
            fill="#828282",
            font=("NunitoSans SemiBold", 10 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            510.0,
            197.5,
            image=entry_image_1
        )
        entry_email = Entry(
            bd=0,
            bg="#D6EFDA",
            fg="#000716",
            highlightthickness=0
        )
        entry_email.place(
            x=397.0,
            y=185.0,
            width=226.0,
            height=23.0
        )

        canvas.create_text(
            393.0,
            222.0,
            anchor="nw",
            text="Username",
            fill="#828282",
            font=("NunitoSans SemiBold", 10 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            510.0,
            252.5,
            image=entry_image_2
        )
        entry_user = Entry(
            bd=0,
            bg="#D6EFDA",
            fg="#000716",
            highlightthickness=0
        )
        entry_user.place(
            x=397.0,
            y=240.0,
            width=226.0,
            height=23.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            510.0,
            306.5,
            image=entry_image_3
        )
        entry_password = Entry(
            bd=0,
            bg="#D6EFDA",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        entry_password.place(
            x=397.0,
            y=294.0,
            width=226.0,
            height=23.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=393.0,
            y=332.0,
            width=12.0,
            height=12.0
        )

        canvas.create_text(
            413.0,
            332.5,
            anchor="nw",
            text="Remember Me",
            fill="#A1A1A1",
            font=("NunitoSans Regular", 8 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            433.0,
            133.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            412.0,
            62.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        Registro = Button(
            image=button_image_2,
            #borderwidth=0,
            highlightthickness=0,
            #command=lambda: print("Registro clicked"),
            #relief="flat"
            text="Registrarse",
            command=register,
            bd=0,
            bg="#D6EFDA",
            fg="#000716",
        )
        Registro.place(
            x=390.0,
            y=363.0,
            width=240.0,
            height=31.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            196.0,
            221.0,
            image=image_image_3
        )
        window_register.resizable(False, False)   
        window_register.mainloop()

    #LOGIN
    window_login = Tk()
    window_login.geometry("662x444")
    window_login.configure(bg = "#F0F8F8")


    #Diseño Login
    canvas = Canvas(
        window_login,
        bg = "#F0F8F8",
        height = 444,
        width = 662,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    login = Button(
        image=button_image_1,
        #borderwidth=0,
        highlightthickness=0,
        #command=lambda: print("button_1 clicked"),
        #relief="flat"
        text="Login",
        command=login,
        bd=0,
        bg="#D6EFDA",
        fg="#000716",
    )
    login.place(
        x=390.0,
        y=301.0,
        width=240.0,
        height=31.0
    )


    canvas.create_text(
        393.0,
        167.0,
        anchor="nw",
        text="Email or Username",
        fill="#828282",
        font=("NunitoSans SemiBold", 10 * -1)
    )

    canvas.create_text(
        393.0,
        224.0,
        anchor="nw",
        text="Password",
        fill="#828282",
        font=("NunitoSans SemiBold", 10 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        510.0,
        197.5,
        image=entry_image_1
    )
    email_user = Entry(
        bd=0,
        bg="#D6EFDA",
        fg="#000716",
        highlightthickness=0
    )
    email_user.place(
        x=397.0,
        y=185.0,
        width=226.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        510.0,
        254.5,
        image=entry_image_2
    )
    password_user = Entry(
        bd=0,
        bg="#D6EFDA",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    password_user.place(
        x=397.0,
        y=242.0,
        width=226.0,
        height=23.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=393.0,
        y=275.0,
        width=12.0,
        height=12.0
    )

    canvas.create_text(
        413.0,
        275.5,
        anchor="nw",
        text="Remember Me",
        fill="#A1A1A1",
        font=("NunitoSans Regular", 8 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        502.0,
        133.0,
        image=image_image_1
    )

    canvas.create_text(
        414.0,
        384.0,
        anchor="nw",
        text="Not Registered Yet?",
        fill="#828282",
        font=("NunitoSans Regular", 10 * -1)
    )

    #REGISTRO POR MEDIO DE LOGIN
    def registroL():
        window_login.destroy()
        window_register()

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    registroL = Button(
        image=button_image_3,
        #borderwidth=0,
        highlightthickness=0,
        #command=lambda: print("button_3 clicked"),
        #relief="flat"
        text="RegistroL",
        command=registroL,
        bd=0,
        bg="#D6EFDA",
        fg="#000716",
    )
    registroL.place(
        x=510.0,
        y=384.0,
        width=82.0,
        height=14.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        412.0,
        62.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        197.0,
        222.0,
        image=image_image_3
    )

    window_login.resizable(False, False)
    window_login.mainloop()
    
windows_login_w()