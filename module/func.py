import json

getInfo = lambda: json.load (open ("files/equipos.json")) # para obtener el archivo .json como diccionario

capitalizedList = lambda lst: list (map (capitalizeValues, lst)) # nueva lista con los valores del diccionario capitalizados

capitalizeValues = lambda elem: dict (zip (elem.keys(), list (map (capitalizeFunc, elem.values())))) # nuevo diccionario con los valores capitalizados

capitalizeFunc = lambda val: " ".join([word.capitalize() for word in val.split()]) if type(val) == str else val # si el elemento es String, lo capitaliza. si no, lo devuelve tal y como está

def overwrite(newFile): # para crear el nuevo archivo
    with open ("files/equipos.json", "w") as file:
        file.write (json.dumps (capitalizedList (newFile), indent = 4, sort_keys = True))
        file.close()