import random

# Ejercicio 2.1
print("Ejercicio 2.1: Números del 1 al 20 en orden inverso:")
numero = 20
while numero >= 1:
    print(numero)
    numero -= 1

# Ejercicio 2.2
print("\nEjercicio 2.2: Números de 2 en 2 hasta el 50:")
numero = 2
while numero <= 50:
    print(numero)
    numero += 2

# Ejercicio 2.3
print("\nEjercicio 2.3: Contar vocales en una cadena:")
cadena = input("Ingrese una cadena: ").lower()
vocales = "aeiou"
contador_vocales = 0
indice = 0

while indice < len(cadena):
    if cadena[indice] in vocales:
        contador_vocales += 1
    indice += 1

print("Número de vocales en la cadena:", contador_vocales)

# Ejercicio 2.4
print("\nEjercicio 2.4: Tirar un dado hasta obtener un 6:")
tirada = 0
contador_tiradas = 0

while tirada != 6:
    tirada = random.randint(1, 6)
    contador_tiradas += 1
    print("Tirada:", tirada)

print("Se necesitó tirar el dado", contador_tiradas, "veces para obtener un 6.")

# Ejercicio 2.5
print("\nEjercicio 2.5: Sumar los dígitos de un número:")
numero_str = input("Ingrese un número: ")
suma_digitos = 0
indice = 0

while indice < len(numero_str):
    suma_digitos += int(numero_str[indice])
    indice += 1

print("La suma de los dígitos es:", suma_digitos)