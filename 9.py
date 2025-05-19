dict = {
    "nombre": "rida",
    "apellidos":  "adel",
    "edad": "18",
    "aficiones": "jugar futbol, baloncesto",
    "ciudad": "Porto" # type
}

clave_buscada = input("Introduce la clave que quieres consultar: ")

if clave_buscada in dict:
    valor = dict[clave_buscada]
    print(f"El valor asociado a la clave '{clave_buscada}' es: {valor}")
else:
    print(f"La clave '{clave_buscada}' no existe en el diccionario.")