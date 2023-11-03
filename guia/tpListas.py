# Ejercicio 1

def ingresarArray(num1, num2):
    lista = []
    numero = int(input("Ingrese un numero en el array: "))
    while numero != -1:
        if numero >= num1 and numero <= num2:
            lista.append(numero)
        elif numero < num1 or numero > num2:
            print(f"El numero {numero} no se puede agregar a la lista")
        numero = int(input("Ingrese un numero en el array: "))
    print(lista)

# Ejercicio 2

def ingresarArray(num1, num2):
    lista = []
    numero = int(input("Ingrese un numero en el array: "))
    while numero != -1:
        if numero >= num1 and numero <= num2:
            lista.append(numero)
        elif numero < num1 or numero > num2:
            print(f"El numero {numero} no se puede agregar a la lista")
        numero = int(input("Ingrese un numero en el array: "))
    sumaTotal = 0
    for i in range(len(lista)):
        sumaTotal += lista[i]   
    print(sumaTotal)
    print(lista)

# Ejercicio 4

def buscarRepetido(numeros, numeroAbuscar):
    numRepetido = 0
    for i in range(len(numeros)):
        if numeros[i] == numeroAbuscar:
            numRepetido += 1
    print(numRepetido)

# arra = [10, 10, 20, 30, 40, 10, 50, 40]
# buscarRepetido(arra, 40)

# Ejercicio 5 

def invertirArray(array):
    nuevoArray = []
    for i in range(len(array)):
        nuevoArray.insert(0, array[i])
    return print(nuevoArray) 

# lista2 =  [5, 7, 1] #1 7 5
# invertirArray(lista2)


# def burbujas(lista1):
#     for i in range(0, len(lista1) - 1):
#         for j in range(0, len(lista1) - 1 - i):
#             if lista1[j] > lista1[j + 1]:
#                 lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
#     return lista1

# lista = [1, 3, 4, 9, 30, 20, 15]
# lista_ordenada = burbujas(lista)

# print(lista_ordenada)


def burbujeo(lista):
    for i in range(len(lista) -1):
        for j in range(len(lista) -1-i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

mi_lista = [64, 34, 25, 12, 22, 11, 90]

# burbujeo(mi_lista)

# print("Lista ordenada:")
# print(mi_lista)

def busquedaPosiciones(numero, lista):
    pos = -1 # siempre que no se encuentre numero la posicion va a ser -1
    i = 0
    while pos == -1 and i < len(lista): 
        if lista[i] == numero: # si el iterador en la lista trae el mismo numero que se paso como parametro
            pos = i # la posicion se iguala
        i = i+1 # si no es igual se suma y se ejecuta el ciclo de nuevo
    print(pos)
    return pos

# Ejercicio 6 

def busquedaPosiciones(numero, lista):
    pos = []
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            pos.append(i)
        i = i+1
    print(pos)
    return pos

# Ejercicio 8 

import random


def aleatorio():
    lista = []
    terminado = False
    while terminado == False:
        aleatorio2 = random.randint(0, 100)
        if aleatorio2 == 0:
            terminado = True
        else:
            lista.append(aleatorio2)
            print(lista)
# aleatorio()


def noRepetidos():
    lista = []
    cantidad = int(input("Ingrese a cantidad de numeros: "))
    for i in range(cantidad):
        lista.append(random.randint(0, 100))
    for j in range( i +1, len(lista)):
        if lista[j] == lista[j]:
            print("hay repetido")
            return True
    print(lista)
noRepetidos()

# dados 5 numeros, ingresarlos y calcular promedio
# imprimir los num que estaban por arriba del promedio

# def suma():
#     cant = 5
#     lista = [] 
#     for i in range(cant):
#         numero = int(input("ingrese un numero: "))
#         lista.append(numero)
#     print(lista)
#     total = 0
#     for j in range(len(lista)):
#         total = total + lista[j]
#     print("Total: ", total)
#     promedio = total / cant
#     print("promedio: ", promedio)
#     mayorProm = []
#     for k in range(len(lista)):
#         if lista[k] > promedio:
#             mayorProm.append(lista[k])
#     print("Mayores que el prom: ", mayorProm)
    
# suma()