informacion_personal = {
    "nombre": "Jonathan Alvarez",
    "edad": 19,
    "ciudad": "Francisco de Orellana",
    "profesion": "Mecánico automotriz"
}

informacion_personal["ciudad"] = "Quito"

if "telefono" in informacion_personal:
    print("La clave 'telefono' ya existe.")
else:
    informacion_personal["telefono"] = "0923433578"

del informacion_personal["edad"]

print("Diccionario final:", informacion_personal)
