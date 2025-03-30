def obtener_informacion():
    return {
        "nombre": input("Ingresa tu nombre: "),
        "edad": int(input("Ingresa tu edad: ")),
        "ciudad": input("Ingresa tu ciudad: "),
        "profesion": input("Ingresa tu profesión: ")
    }

print("Elige una opción:")
print("1. Usar datos predeterminados")
print("2. Ingresar nuevos datos")

opcion = input("Opción (1/2): ")

if opcion == "1":
    informacion_personal = {
        "nombre": "Jonathan Alvarez",
        "edad": 19,
        "ciudad": "Francisco de Orellana",
        "profesion": "Mecánico automotriz"
    }
elif opcion == "2":
    informacion_personal = obtener_informacion()
else:
    print("Opción no válida. Usando datos predeterminados.")
    informacion_personal = {
        "nombre": "Jonathan Alvarez",
        "edad": 19,
        "ciudad": "Francisco de Orellana",
        "profesion": "Mecánico automotriz"
    }

informacion_personal["ciudad"] = "Quito"

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0923433578"

del informacion_personal["edad"]

print("Diccionario final:", informacion_personal)
