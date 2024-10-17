# Ejercicio 1.1
letra = input("Ingrese una letra: ").lower()
if letra >= 'a' and letra <= 'm':
    print("La letra es de las primeras letras del alfabeto.")
elif letra >= 'n' and letra <= 'z':
    print("La letra es de las últimas letras del alfabeto.")
else:
    print("Entrada no válida. Por favor, ingrese una letra del alfabeto.")

# Ejercicio 1.2
angulo = float(input("Ingrese el valor de un ángulo en grados: "))
if angulo > 0 and angulo < 90:
    print("El ángulo se encuentra en el primer cuadrante.")
elif angulo > 90 and angulo < 180:
    print("El ángulo se encuentra en el segundo cuadrante.")
elif angulo > 180 and angulo < 270:
    print("El ángulo se encuentra en el tercer cuadrante.")
elif angulo > 270 and angulo < 360:
    print("El ángulo se encuentra en el cuarto cuadrante.")
elif angulo == 0 or angulo == 360:
    print("El ángulo está en el eje positivo del eje X.")
elif angulo == 180:
    print("El ángulo está en el eje negativo del eje X.")
elif angulo == 90:
    print("El ángulo está en el eje positivo del eje Y.")
elif angulo == 270:
    print("El ángulo está en el eje negativo del eje Y.")
else:
    print("El ángulo está fuera de los límites de un círculo (0-360 grados).")

# Ejercicio 1.3
calificacion = float(input("Ingrese la calificación del estudiante: "))
if calificacion > 4.5:
    print("Rendimiento: Excelente")
elif 3.5 <= calificacion <= 4.5:
    print("Rendimiento: Bueno")
elif 3 <= calificacion < 3.5:
    print("Rendimiento: Regular")
elif 0 <= calificacion < 3:
    print("Rendimiento: Insuficiente")
else:
    print("Calificación no válida. Debe estar entre 0 y 5.")

# Ejercicio 1.4
temperatura = float(input("Ingrese la temperatura: "))
if temperatura < 15:
    print("Temperatura: Frío")
elif 15 <= temperatura < 25:
    print("Temperatura: Templado")
else:
    print("Temperatura: Cálido")

# Ejercicio 1.5
palabra = input("Ingrese la palabra 'Jengibre': ")
if palabra == "Jengibre":
    print("Sí, ¡El Jengibre es la mejor planta de todos los tiempos!")
elif palabra == "jengibre":
    print("No, ¡quiero un gran Jengibre!")
else:
    print("¡Jengibre! No", palabra)