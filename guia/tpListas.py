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

lista2 =  [5, 7, 1] #1 7 5
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

def burbujeo2(lista):
    for i in range(len(lista) -1):
        for j in range(len(lista) -1 -i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                
mi_lista = [64, 34, 25, 12, 22, 11, 90]
burbujeo2(mi_lista)
print(mi_lista)