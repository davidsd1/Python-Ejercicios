# Ejercicio 3.1
suma_cubos = 0
for numero in range(1, 51):
    suma_cubos += numero ** 3

print("La suma de los cubos de los números del 1 al 50 es:", suma_cubos)

# Ejercicio 3.2
print("\nEjercicio 3.2: Pirámide de asteriscos")
for i in range(1, 6):
    print('*' * i)

# Ejercicio 3.3
print("\nEjercicio 3.3: Tablero de ajedrez")
for fila in range(8):
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            print("█", end=" ")  # Casilla negra
        else:
            print(" ", end=" ")  # Casilla blanca
    print()  # Nueva línea al final de cada fila

# Ejercicio 3.4
cadena = input("\nEjercicio 3.4: Ingrese una cadena para invertir: ")
cadena_invertida = ""
for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]

print("La cadena invertida es:", cadena_invertida)

# Ejercicio 3.5
lista_caracteres = ['carro', 'bicicleta', 'moto', 'avión']
elemento_buscado = input("\nEjercicio 3.5: Ingrese un elemento a buscar en la lista: ")

encontrado = False
for elemento in lista_caracteres:
    if elemento == elemento_buscado:
        encontrado = True
        break

if encontrado:
    print(f"El elemento '{elemento_buscado}' fue encontrado en la lista.")
else:
    print(f"El elemento '{elemento_buscado}' no se encuentra en la lista.")