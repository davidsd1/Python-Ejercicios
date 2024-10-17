# Ejercicio 4.1
suma = lambda x, y: x + y
resultado_suma = suma(5, 3)
print("La suma de 5 y 3 es:", resultado_suma)

# Ejercicio 4.2
es_par = lambda x: x % 2 == 0
numero = 4
print(f"¿El número {numero} es par?", es_par(numero))

# Ejercicio 4.3
lista_tuplas = [(1, 3), (2, 1), (4, 2)]
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
print("Lista de tuplas ordenada según el segundo elemento:", lista_tuplas_ordenada)

# Ejercicio 4.4
lista_numeros = [5, 12, 3, 18, 7, 10, 15]
numeros_mayores_a_10 = list(filter(lambda x: x > 10, lista_numeros))
print("Números mayores a 10:", numeros_mayores_a_10)

# Ejercicio 4.5
numeros = [1, 2, 3, 4, 5]
numeros_cuadrados = list(map(lambda x: x ** 2, numeros))
print("Números elevados al cuadrado:", numeros_cuadrados)