import random

lista = []

def agregarNumeros():
    hasta = int(input("Ingrese la cantidad de numeros en la lista: "))
    for i in range(0, hasta):
        lista.append(random.randint(0, hasta))


def repetido(arr):
    repetidos = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if lista[i] not in repetidos:
                    repetidos.append(lista[i])
    print(repetidos)
    return False
    
    
    
def busqueda(lista, numero):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == numero:
            pos = 1
        i = i+1
    return pos

agregarNumeros()
print(lista)
repetidos = repetido(lista)



