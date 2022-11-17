import tkinter as tk
from tkinter import messagebox
from consult import interfaz_equipo
from module.func import getInfo

def crear_interfaz(app): # creando la nueva interfaz de consulta
    varGetEntry = tk.StringVar() # variable para getear el entry
    form_consultEquipo = tk.Toplevel(app, width = 410, height = 150) # creando la nueva ventana

    getEquipo = lambda nombre: list (filter (lambda equipo: equipo['nombreEquipo'] == nombre, getInfo ())) # filtra los equipos que coincidan con el nombre ingresado

    def funcionPrincipal(): # consultamos el equipo: si existe, creamos una interfaz para mostrar sus datos. si no existe, mostramos un msj de error
        try:
            interfaz_equipo.crear_interfaz(form_consultEquipo, getEquipo(varGetEntry.get())[0]) # llamamos a la interfaz que muestra los elementos
        except:
            messagebox.showerror('Error', '¡El equipo no existe!')

    lblFrEquipo = lambda: tk.LabelFrame (form_consultEquipo, text = " Consulta del Equipo ", width = 400, height = 140, # creando el labelframe
                                         labelanchor = 'n').pack (padx = 10, pady = 10)

    lblNombreEquipo = lambda: tk.Label (form_consultEquipo, text = "Nombre del equipo: ", font = ('Arial', 12), # label del nombre de equipo
                                        width = 20).place (x = 15, y = 45)
    
    entryNombreEquipo = lambda: tk.Entry (form_consultEquipo, font = ('Arial', 12), textvariable = varGetEntry, # entry del nombre de equipo
                                          width = 20). place(x = 190, y = 47)
    
    btnAceptar = lambda: tk.Button(form_consultEquipo, text = "  Buscar  ", font = ('Arial', 12), bg = "#77DD77", # boton de aceptación
                                   command = funcionPrincipal). place (x = 170, y = 89)

    lblFrEquipo(), lblNombreEquipo(), entryNombreEquipo(), btnAceptar() # llamamos las funciones