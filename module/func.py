import json

getInfo = lambda: json.load (open ("files/equipos.json")) # para obtener el archivo .json como diccionario

capitalizeValues = lambda elem: dict (zip 
(elem.keys(), list (map (capitalizeFunc, elem.values())))) 
# se mapea el diccionario para obtener los valores capitalizados

capitalizeFunc = lambda val: " ".join([
word.capitalize() for word in val.split()]) if type(val) == str else val 
# devuelve la lista de los valores capitalizados. Si es string, lo capitaliza.
# si no es string, lo devuelve tal y como entra.

def overwrite(newFile): # para crear el nuevo archivo
    with open ("files/equipos.json", "w") as file:
        file.write (json.dumps (newFile, indent = 3))
        file.close()