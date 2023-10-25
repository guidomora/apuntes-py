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