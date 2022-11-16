import tkinter as tk
from module.func import overwrite, getInfo

def crear_interfaz(app, cantidad, indice):
    lst_vars = [tk.StringVar(), tk.StringVar()] # lista de variables para getear los entrys
    form_jug = tk.Toplevel(app, width = 425, height = 165) # creando la nueva ventana

    getFields = lambda: { # obteniendo los datos de los campos de la interfaz (como diccionario)
                'nombreJugador': lst_vars[0].get(),
                'dniJugador': lst_vars[1].get(),
                'idJugador' : len (getInfo()[indice]['jugadores']) + 1,
                'estado': 'Disponible'
                }

    def formatFile(elem): # para agregar el elemento al diccionario
        lst = getInfo()
        lst[indice]['jugadores'].append(elem)
        return lst

    def recrear(app, cantidad): # recrea la interfaz de forma recursiva para c/ jugador
        form_jug.destroy()
        return crear_interfaz(app, cantidad, indice) if cantidad < 3 else form_jug.destroy()
    
    def funcionPrincipal(): # función que realiza las otras funciones
        overwrite (formatFile (getFields ()))
        recrear(app, cantidad + 1)

    lblFrJugador = lambda: tk.LabelFrame (form_jug, text = " Datos del Jugador ", width = 420, height = 150, # creando el labelframe
                                         labelanchor = 'n').pack (padx = 10, pady = 10)

    lblNombreJugador = lambda: tk.Label (form_jug, text = "Nombre del jugador: ", font = ('Arial', 12), # label del nombre
                                        width = 20).place (x = 15, y = 35)
    
    entryNombreJugador = lambda: tk.Entry (form_jug, font = ('Arial', 12), textvariable = lst_vars[0], # entry del nombre
                                          width = 20). place(x = 205, y = 37)
    
    lblDocumento = lambda: tk.Label (form_jug, text = "DNI del jugador: ", font = ('Arial', 12), # label del DNI
                                           width = 20).place (x = 15, y = 65)
    
    entryDocumento = lambda: tk.Entry (form_jug, font = ('Arial', 12), textvariable = lst_vars[1], # entry del DNI
                                          width = 20). place(x = 205, y = 67)
    
    btnAceptar = lambda: tk.Button(form_jug, text = "  Aceptar  ", font = ('Arial', 12), bg = "#77DD77", # boton de aceptación
                                   command = funcionPrincipal). place (x = 175, y = 110) 
    
    lblFrJugador(), lblNombreJugador(), entryNombreJugador(), lblDocumento(), 
    entryDocumento(), btnAceptar() # llamando a las funciones