
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
