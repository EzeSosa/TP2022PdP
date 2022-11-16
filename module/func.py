import json

getInfo = lambda: json.load (open ("files/equipos.json")) # para obtener el archivo .json como diccionario

def overwrite(newFile): # para crear el nuevo archivo
    with open ("files/equipos.json", "w") as file:
        file.write (json.dumps (newFile, indent = 4, sort_keys = True))
        file.close()