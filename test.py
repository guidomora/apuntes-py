# Busqueda de maximo o minimo (se cambia el signo)


# lista = [1000, 2500, 4200, 3244, 5999]

# for i in range(len(lista)):
#     if i == 0 or lista[i] > maximo:
#         maximo = lista[i]
#         pos = i
# print(maximo, "en la pos", pos)




def busqueda(lista, numero):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == numero:
            pos = i
        i = i+1
    print(pos)
    
    
# lista = [1, 5, 21, 43, 55, 14, 98]

# busqueda(lista, 14)

def maxNum(lista):
    for i in range(len(lista)):
       if i == 0 or lista[i] > maximo:
            maximo = lista[i]
            pos = i
            print("El maximo es: ", maximo)
    return(maximo, pos)
        

def ejercicio(lista):
    cantidad = 10
    for i in range(cantidad):
        numero = int(input("Ingresar :"))
        lista.append(numero)
    maxNum(lista)
    
    
    
    
lista = []
ejercicio(lista)
print(lista)