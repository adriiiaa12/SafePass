# Importar librerías necesarias
import tkinter as tk
import secrets
import string
import copy
import pyperclip
from tkinter import messagebox

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función principal
def createWindow():
    window = tk.Tk()
    window.resizable(0, 0)
    window.geometry("300x160")
    window.iconbitmap("")
    window.title("Generar contraseña")
    window.configure()
    
    # Estilo de botón copiar (bordes)
    estilo_boton_copiar_1 = {
        "bg": "#98FB98", 
        "fg": "black", 
        "bd": 0,
        "relief": "solid",
        "borderwidth": 2,
        "highlightthickness": 0,
        "activebackground": "green",  
        "activeforeground": "white", 
        "highlightbackground": "white", 
        "highlightcolor": "white"  
    }
    
    # Estilo botón copiar 2 (bordes + color fuerte)
    estilo_boton_copiar_2 = {
        "bg": "#00FF00", 
        "fg": "black", 
        "bd": 0, 
        "relief": "solid", 
        "borderwidth": 2, 
        "highlightthickness": 0,
        "activebackground": "green",  
        "activeforeground": "white", 
        "highlightbackground": "white", 
        "highlightcolor": "white"
    }
    
    # Estilo de botón cancelar (bordes)
    estilo_boton_cancelar_1 = {
        "bg": "#FFC0CB", 
        "fg": "black", 
        "bd": 0,
        "relief": "solid",
        "borderwidth": 2,
        "highlightthickness": 0,
        "activebackground": "red",  
        "activeforeground": "white", 
        "highlightbackground": "white", 
        "highlightcolor": "white"  
    }
    
    # Estilo botón cancelar 2 (bordes + color fuerte)
    estilo_boton_cancelar_2 = {
        "bg": "#FF69B4", 
        "fg": "black", 
        "bd": 0, 
        "relief": "solid", 
        "borderwidth": 2, 
        "highlightthickness": 0,
        "activebackground": "red",  
        "activeforeground": "white", 
        "highlightbackground": "white", 
        "highlightcolor": "white"
    }
    
    # Generar contraseña
    contraseña_segura = generar_contraseña(12)
    
    # Función copiarTexto
    def copiarTexto():
        pyperclip.copy(contraseña_segura)
        print("Contraseña copiada: ", contraseña_segura)
        window.destroy()
        tk.messagebox.showinfo("Contraseña copiada", "Se ha copiado correctamente la contraseña")

    # Función cancelar
    def cancelar():
        window.destroy()
    
    # Label título ventana "window"
    label_titulo = tk.Label(window, text="Contraseña segura", font="Helvetica 15")
    label_titulo.pack(pady=15)
    
    # Label contraseña segura
    label_contraseña_segura = tk.Label(window, text=contraseña_segura, fg="black", font="Helvetica 10")
    label_contraseña_segura.pack(pady=10)
    
    # Botón "copiar"
    boton_copiar = tk.Button(window, text="Copiar", **estilo_boton_copiar_1, command=copiarTexto)
    boton_copiar.pack(side="left", padx=30, pady=15)
    
    # Botón "cancelar"
    boton_cancelar = tk.Button(window, text="Cancelar", **estilo_boton_cancelar_1, command=cancelar)
    boton_cancelar.pack(side="right", padx=30, pady=15)
    
    # Funciones para el efecto de sombreado (copiar)
    def on_enter_copiar(event):
        event.widget.config(**estilo_boton_copiar_2)

    def on_leave_copiar(event):
        event.widget.config(**estilo_boton_copiar_1)
        
    # Funciones para el efecto de sombreado (cancelar)
    def on_enter_cancelar(event):
        event.widget.config(**estilo_boton_cancelar_2)

    def on_leave_cancelar(event):
        event.widget.config(**estilo_boton_cancelar_1)

    # Poner las funciones sombreado cursor a los botones
    boton_copiar.bind("<Enter>", on_enter_copiar)
    boton_copiar.bind("<Leave>", on_leave_copiar)

    boton_cancelar.bind("<Enter>", on_enter_cancelar)
    boton_cancelar.bind("<Leave>", on_leave_cancelar)
    
    # Ejecutar loop de la ventana "window"
    window.mainloop()