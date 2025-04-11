nombre = input("Ingresa tu nombre: ")

print("¿Cómo deseas mostrar tu nombre?")
print("1. En mayúsculas")
print("2. En minúsculas")
print("3. Con la primera letra mayúscula")

opcion = input("Ingresa el número de la opción (1, 2 o 3): ")

if opcion == "1":
    nombre_transformado = nombre.upper()
elif opcion == "2":
    nombre_transformado = nombre.lower()
elif opcion == "3":
    nombre_transformado = nombre.title()
else:
    nombre_transformado = "Opción inválida."

print(nombre_transformado)