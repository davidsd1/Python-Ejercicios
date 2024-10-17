def menu():
    while True:
        print("\nMenú de Ejercicios Lambda:")
        print("1. Sumar dos números")
        print("2. Verificar si un número es par")
        print("3. Ordenar una lista de tuplas")
        print("4. Filtrar números mayores a 10")
        print("5. Elevar cada número al cuadrado")
        print("6. Salir")
        
        opcion = input("Por favor, ingrese el número de la opción deseada: ")

        if opcion == '1':
            # Ejercicio 4.1: Sumar dos números
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            suma = lambda a, b: a + b
            resultado_suma = suma(x, y)
            print("La suma es:", resultado_suma)

        elif opcion == '2':
            # Ejercicio 4.2: Verificar si un número es par
            numero = int(input("Ingrese un número: "))
            es_par = lambda x: x % 2 == 0
            print(f"¿El número {numero} es par? {'Sí' if es_par(numero) else 'No'}")

        elif opcion == '3':
            # Ejercicio 4.3: Ordenar una lista de tuplas
            lista_tuplas = [(1, 3), (2, 1), (4, 2)]
            lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
            print("Lista de tuplas ordenada según el segundo elemento:", lista_tuplas_ordenada)

        elif opcion == '4':
            # Ejercicio 4.4: Filtrar números mayores a 10
            lista_numeros = [5, 12, 3, 18, 7, 10, 15]
            numeros_mayores_a_10 = list(filter(lambda x: x > 10, lista_numeros))
            print("Números mayores a 10:", numeros_mayores_a_10)

        elif opcion == '5':
            # Ejercicio 4.5: Elevar cada número al cuadrado
            numeros = [1, 2, 3, 4, 5]
            numeros_cuadrados = list(map(lambda x: x ** 2, numeros))
            print("Números elevados al cuadrado:", numeros_cuadrados)

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elija una opción del menú.")

# Llamar a la función de menú
menu()