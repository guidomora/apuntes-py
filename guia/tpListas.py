# Ejercicio 1

# def ingresarArray(num1, num2):
#     lista = []
#     numero = int(input("Ingrese un numero en el array: "))
#     while numero != -1:
#         if numero >= num1 and numero <= num2:
#             lista.append(numero)
#         elif numero < num1 or numero > num2:
#             print(f"El numero {numero} no se puede agregar a la lista")
#         numero = int(input("Ingrese un numero en el array: "))
#     print(lista)

# Ejercicio 2

# def ingresarArray(num1, num2):
#     lista = []
#     numero = int(input("Ingrese un numero en el array: "))
#     while numero != -1:
#         if numero >= num1 and numero <= num2:
#             lista.append(numero)
#         elif numero < num1 or numero > num2:
#             print(f"El numero {numero} no se puede agregar a la lista")
#         numero = int(input("Ingrese un numero en el array: "))
#     sumaTotal = 0
#     for i in range(len(lista)):
#         sumaTotal += lista[i]   
#     print(sumaTotal)
#     print(lista)

# Ejercicio 4

# def buscarRepetido(numeros, numeroAbuscar):
#     numRepetido = 0
#     for i in range(len(numeros)):
#         if numeros[i] == numeroAbuscar:
#             numRepetido += 1
#     print(numRepetido)

# arra = [10, 10, 20, 30, 40, 10, 50, 40]
# buscarRepetido(arra, 40)

# Ejercicio 5 

def invertirArray(array):
    nuevoArray = []
    for i in range(len(array)):
        nuevoArray.insert(0, array[i])
    return print(nuevoArray) 

lista2 =  [5, 7, 1] #1 7 5
invertirArray(lista2)