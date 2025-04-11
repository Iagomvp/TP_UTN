magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"

print(f"Clasificación: {clasificacion}")