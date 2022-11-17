import tkinter as tk

def crear_interfaz(app, obj): # creando la nueva interfaz para los equipos
    form_datosEquipo = tk.Toplevel(app, width = 410, height = 445) # creando la nueva ventana

    lblFrDatosEquipo = lambda: tk.LabelFrame (form_datosEquipo, text = " Datos del Equipo ", width = 400, height = 150, # creando el labelframe
                                              labelanchor = 'n').pack (padx = 10, pady = 5)
    
    def mostrar_jugadores(id, desp):
        tk.Label (form_datosEquipo, text = f"{obj['jugadores'][id]['idJugador']}", font = ('Arial', 11)). place (x = 20, y = 210 + desp) # ID del jugador obtenido
        tk.Label (form_datosEquipo, text = f"{obj['jugadores'][id]['nombreJugador']}", font = ('Arial', 11)). place (x = 80, y = 210 + desp) # nombre del jugador obtenido
        tk.Label (form_datosEquipo, text = f"{obj['jugadores'][id]['dniJugador']}", font = ('Arial', 11)). place (x = 310, y = 210 + desp) # DNI del jugador obtenido
        return mostrar_jugadores(id + 1, desp + 20) if id + 1 < len(obj['jugadores']) else 0 # se llama recursivamente

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
    
    lblFrJugadores = lambda: tk.LabelFrame (form_datosEquipo, text = " Jugadores ", width = 400, height = 280, # labelframe de los jugadores
                                            labelanchor = 'n').pack (padx = 10, pady = 10)
    
    lblIdJug = lambda: tk.Label (form_datosEquipo, text = "ID", font = ('Arial', 12)).place (x = 20, y = 200) # ID jugadores
    lblNombreJug = lambda: tk.Label (form_datosEquipo, text = "NOMBRE", font = ('Arial', 12)).place (x = 80, y = 200) # NOMBRE jugadores
    lblDNIJug = lambda: tk.Label (form_datosEquipo, text = "DNI", font = ('Arial', 12)).place (x = 310, y = 200) # DNI jugadores

    lblFrDatosEquipo(), lblNombre(), lblId(),
    lblDireccion(), lblLocalidad(), lblNombreRespo(),
    lblFrJugadores(), lblIdJug(), lblNombreJug(), lblDNIJug(),
    mostrar_jugadores(0, 15) # llamando las funciones