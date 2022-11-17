import tkinter as tk
from registers import registrar_jugadores
from module.func import overwrite, getInfo, capitalizeValues # funciones importadas del módulo de funciones

def crear_interfaz(app): # creando la interfaz de registro
    lst_vars = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()] # lista de variables para getear los entrys
    form_equipo = tk.Toplevel(app, width = 410, height = 280) # creando la nueva ventana

    getFields = lambda: { # obteniendo los datos de los campos de la interfaz (como diccionario)
                'idEquipo': len (getInfo()) + 1,
                'nombreEquipo': lst_vars[0].get(),
                'direccionEquipo': lst_vars[1].get(),
                'localidadEquipo': lst_vars[2].get(),
                'nombreResponsable': lst_vars[3].get(),
                'jugadores': [],
                }

    def formatFile(elem): # agregando un equipo a la lista de equipos
        lst = getInfo()
        lst.append(capitalizeValues (elem))
        return lst
    
    def funcionPrincipal(): # función que realiza las funciones
        registrar_jugadores.crear_interfaz(form_equipo, 0, len(formatFile (getFields())) - 1) # abriendo la nueva interfaz de registro de jugadores
        overwrite (formatFile (getFields ())) # sobreescribiendo el archivo del equipo

    lblFrEquipo = lambda: tk.LabelFrame (form_equipo, text = " Datos del Equipo ", width = 405, height = 225, # creando el labelframe
                                         labelanchor = 'n').pack (padx = 10, pady = 10)
    
    lblNombreEquipo = lambda: tk.Label (form_equipo, text = "Nombre del equipo: ", font = ('Arial', 12), # labels y entrys correspondientes
                                        width = 20).place (x = 20, y = 35)
    
    entryNombreEquipo = lambda: tk.Entry (form_equipo, font = ('Arial', 12), textvariable = lst_vars[0], # entry del nombre
                                          width = 20). place(x = 210, y = 37)
    
    lblDireccionEquipo = lambda: tk.Label (form_equipo, text = "Dirección del equipo: ", font = ('Arial', 12), # label de la dirección
                                           width = 20).place (x = 20, y = 65)
    
    entryDireccionEquipo = lambda: tk.Entry (form_equipo, font = ('Arial', 12), textvariable = lst_vars[1], # entry de la dirección
                                          width = 20). place(x = 210, y = 67)
    
    lblLocalidadEquipo = lambda: tk.Label (form_equipo, text = "Localidad del equipo: ", font = ('Arial', 12), # label de la localidad
                                           width = 20).place (x = 20, y = 95)
    
    entryLocalidadEquipo = lambda: tk.Entry (form_equipo, font = ('Arial', 12), textvariable = lst_vars[2], # entry de la localidad
                                          width = 20). place(x = 210, y = 97)

    lblNombreResponsable = lambda: tk.Label (form_equipo, text = "Nombre del responsable: ", font = ('Arial', 12), # label del responsable
                                           width = 20).place (x = 20, y = 125)
    
    entryNombreResponsable = lambda: tk.Entry (form_equipo, font = ('Arial', 12), textvariable = lst_vars[3], # entry del responsable
                                               width = 20). place(x = 210, y = 127)
    
    btnCancelar = lambda: tk.Button(form_equipo, text = "  Cancelar  ", font = ('Arial', 12), bg = "#77DD77",
                                    command = lambda: form_equipo.destroy ()). place (x = 50, y = 180)

    btnRegistrarJugadores = lambda: tk.Button(form_equipo, text = " Registrar Jugadores [11] ", font = ('Arial', 12), bg = "#77DD77",
                                              command = funcionPrincipal). place (x = 183, y = 180)
    
    lblFrEquipo(), lblNombreEquipo(), entryNombreEquipo(), lblDireccionEquipo(), entryDireccionEquipo(), lblLocalidadEquipo(),
    entryLocalidadEquipo(), lblNombreResponsable(), entryNombreResponsable(), btnCancelar(), btnRegistrarJugadores()  # llamando las funciones