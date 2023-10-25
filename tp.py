#Codigo de busqueda binaria

numbers = [0, 10, 50, 23, 52, 91, 72, 14, 38] # lista con los numeros disponibles
numbers.sort() # se ordenan los numeros de mayor a menor
print(numbers) # se los imprime para ver como estan ordenados

def busqueda(value):
    start = 0
    end = len(numbers) - 1 # se resta para que quede igual al indice final
    while start <= end:
        pointer = (start + end) // 2 # punto medio
        if value == numbers[pointer]: # si el valor ingresado es igual al numero con la posicion que indica el pointer
            return pointer # retorna el pointer
        elif value > numbers[pointer]: #si el valor es mayor
            start = pointer + 1 # se actualiza el valor de inicio 
        else:
            end = pointer - 1 # se actualiza el valor de fin 
    return None # si no cumple la condicion del while no retorna nada

def searchValue(value):
    result = busqueda(value)
    if result is None:
        return print(f"El valor {value} no se encontro")
    else:
        return print(f"El valor {value} se encuentra en la posicion {result}")

searchValue(38)

'''
SELECTION SORT
'''

def selection_sort(lista):
  for i in range(0, len(lista)-1):
    pos_minimo = i 
    for j in range(i+1, len(lista)): 
      if (lista[j] < lista[pos_minimo]):
        pos_minimo = j 
    if (pos_minimo != i):
      aux = lista[pos_minimo]
      lista[pos_minimo] = lista[i]
      lista[i] = aux
  return lista

numeros = [1,3,4,-5,10,-2,5]
numeros_ordenados = selection_sort(numeros)
print(f'Lista ordenada por selection sort: {numeros_ordenados}')


# funciona seleccionando repetidamente el elemento mínimo de la lista no ordenada y 
# moviéndolo a la posición correcta en la lista ordenada. En cada iteración, 
# busca el elemento mínimo en la sublista no ordenada y lo intercambia con el elemento en la posición actual 

'''
INSERTION SORT
'''

def insertion_sort(lista):
  for j in range(1, len(lista)):
    i = j - 1
    pos_actual = j #La variable pos_actual la usamos para cuando tenemos mas de 1 swap por iteracion
    while (i >= 0):
      if (lista[i] > lista[pos_actual]):
        aux = lista[pos_actual]
        lista[pos_actual] = lista[i]
        lista[i] = aux
        pos_actual = i
      i = i - 1
  return lista

numeros = [1,3,4,-5,10,-2,5]
numeros_ordenados = insertion_sort(numeros)
print(f'Lista ordenada por insertion sort: {numeros_ordenados}')

# Insertion Sort funciona dividiendo la lista en una sublista ordenada 
# y una sublista no ordenada. Comienza con la sublista ordenada que contiene el primer 
# elemento de la lista. Luego, en cada iteración, toma un elemento de la sublista no ordenada
# y lo coloca en la posición correcta en la sublista ordenada
