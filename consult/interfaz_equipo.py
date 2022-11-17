import tkinter as tk

def crear_interfaz(app, obj): # creando la nueva interfaz para los equipos
    form_datosEquipo = tk.Toplevel(app, width = 410, height = 160) # creando la nueva ventana

    lblFrDatosEquipo = lambda: tk.LabelFrame (form_datosEquipo, text = " Datos del Equipo ", width = 400, height = 150, # creando el labelframe
                                              labelanchor = 'n').pack (padx = 10, pady = 10)
    
    lblNombre = lambda: tk.Label (form_datosEquipo, text = f" Nombre del equipo: {obj['nombreEquipo']}", # nombre del equipo
                          font = ('Arial', 12)).place (x = 20, y = 41)

    lblId = lambda: tk.Label (form_datosEquipo, text = f" ID del equipo: {obj['idEquipo']}", # ID del equipo
                          font = ('Arial', 12)).place (x = 20, y = 61)
    
    lblDireccion = lambda: tk.Label (form_datosEquipo, text = f" Dirección del equipo: {obj['direccionEquipo']}", # dirección del equipo
                          font = ('Arial', 12)).place (x = 20, y = 81)
    
    lblLocalidad = lambda: tk.Label (form_datosEquipo, text = f" Nombre del equipo: {obj['localidadEquipo']}", # localidad del equipo
                          font = ('Arial', 12)).place (x = 20, y = 101)
    
    lblNombreRespo = lambda: tk.Label (form_datosEquipo, text = f" Nombre del responsable: {obj['nombreResponsable']}", # responsable del equipo
                          font = ('Arial', 12)).place (x = 20, y = 121)

    lblFrDatosEquipo(), lblNombre(), lblId(),
    lblDireccion(), lblLocalidad(), lblNombreRespo() # llamando las funciones