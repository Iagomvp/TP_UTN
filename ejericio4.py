edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12:
    categoria = "Niño/a"
elif edad < 18:
    categoria = "Adolescente"
elif edad < 30:
    categoria = "Adulto/a joven"
else:
    categoria = "Adulto/a"

print(f"Perteneces a la categoría: {categoria}")