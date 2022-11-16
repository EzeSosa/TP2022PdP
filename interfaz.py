import tkinter as tk
from registers import registrar_equipo
from consult import consultar_equipo

app = tk.Tk() # creando la ventana
config = lambda: app.config(height = 150, width = 370) # config de la ventana

labelfr = lambda: tk.LabelFrame (app, text = " Federación de Hockey ", width = 370, height = 150, # creando el labelframe
                                  labelanchor = 'n').pack (padx = 10, pady = 10)

regis_equipo = lambda: tk.Button (app, text = 'Registrar Equipo', bg = "#77DD77", # creando el boton para registrar multas
                                  command = lambda: registrar_equipo.crear_interfaz(app), # llamando la función para la nueva ventana
                                  width = 15, font = ('Arial', 12)).place (x = 40, y = 100)

regis_multa = lambda: tk.Button(app, text = 'Consultar Equipo', bg = "#77DD77", # creando el boton para registrar multas
                                command = lambda: consultar_equipo.crear_interfaz(app), # llamando a la interfaz
                                width = 15, font = ('Arial', 12)).place (x = 200, y = 100)

config(), labelfr(), regis_equipo(), regis_multa() # llamando a las funciones
app.mainloop() # para cargar la ventana