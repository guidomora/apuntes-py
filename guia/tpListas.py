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

def suma():
    cant = 5
    lista = [] 
    for i in range(cant):
        numero = int(input("ingrese un numero: "))
        lista.append(numero)
    print(lista)
    total = 0
    for j in range(len(lista)):
        total = total + lista[j]
    print("Total: ", total)
    promedio = total / cant
    print("promedio: ", promedio)
    mayorProm = []
    for k in range(len(lista)):
        if lista[k] > promedio:
            mayorProm.append(lista[k])
    print("Mayores que el prom: ", mayorProm)
    
# suma()

# -----------------------------------

# ingresar 10 elementos usando la funcion de carga y determinar el max
# mediante una funcion 

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
    
# Ejercicio 2 py pdf de listas



def search(val, lista):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == val:
            pos = i
        i = i + 1
    print(pos)
    return pos

def maX(lista):
    for i in range(len(lista)):
        if i == 0 or lista[i] > maximo:
            maximo = lista[i]
    print("El precio maximo es: $",maximo)
    return maximo


productos = []
precios = []

def carga(cant):
    while len(productos) < cant:
        producto = int(input("Ingrese un producto: "))
        precio = int(input("Ingrese un precio: "))
        exists = search(producto, productos)
        if producto > 99 and precio > 0 and exists == -1:
            productos.append(producto)
            precios.append(precio)
        else :
            print("nooo")
        
    for i in range(cant):
        print("Producto: ", productos[i], "--Precio-->", precios[i]) 
        
def busquedaPrecio(lista):
    codProd = 0
    while codProd != -1:
        codProd = int(input("Codigo a buscar (inrese -1 para terminar): "))
        if codProd == -1:
            print("Terminado")
        else :
            pos = search(codProd, lista)
            if pos == -1:
                print("Producto no encontrado")
            else :
                print(precios[pos])
        
    
    
carga(4)
busquedaPrecio(productos)
maX(precios)

# --------------------------------------

# Ejercicio 1 tps finales

legajos = []
notas = []

def cargaDatos():
    legajo = 0
    while legajo != -1:
        legajo = int(input("Ingrese un numero de legajo: "))
        nota = int(input("Ingrese la nota del alumno: "))
        if legajo > 0 and nota > 0 and nota <= 10:
            legajos.append(legajo)
            notas.append(nota)



def showNotas():
    for i in range (len(notas)):
        print(legajos[i],"---------->",notas[i])    

def cuatroMas():
    masQueCuatro = []
    for i in range (len(notas)):
        if notas[i] >= 4:
            masQueCuatro.append(notas[i])
    print("cantidad de alumnos que aprobaron: ", len(masQueCuatro))
    
    

def cuatroMenos():
    menosQueCuatro = []
    for i in range (len(notas)):
        if notas[i] < 4:
            menosQueCuatro.append(notas[i])
    print("cantidad de alumnos que desaprobaron: ", len(menosQueCuatro))

def promedio():
    notasProm = 0
    for i in range(len(notas)):
        notasProm = notas[i] + notasProm   
    promedioTotal = notasProm / len(notas)
    print("La nota promedio es: ", promedioTotal)
    return promedioTotal
        
def masDelProm():
    masProm = []
    legajosMasProm = []
    prom = promedio()
    for i in range(len(notas)):
        if notas[i] >= prom:
            masProm.append(notas[i])
            legajosMasProm.append(legajos[i])
    for i in range(len(masProm)):
        print(legajosMasProm[i],"---->",masProm[i])

cargaDatos()
showNotas()
cuatroMas()
cuatroMenos()
promedio()
masDelProm()

# ------------------------------------------------------

# Ejercicio 2 tps finales 

unidades= []
metrosTotales = []
expensas = []

def busqueda(value, list):
    pos = -1
    i = 0
    while pos == -1 and i < len(list):
        if list[i] == value:
            pos = i
        i = i+1
    return pos

def ingresoDatos():
    i = 0
    while i < 3:
        unidad =  input("Inrese una unidad: ")
        metros = int(input("Ingrese la cantidad de metros cuadrados: "))
        exists = busqueda(unidad, unidades)
        if exists == -1:
            unidades.append(unidad)
            metrosTotales.append(metros)
            i += 1
    for i in range(len(unidades)):
        print("unidad: ",unidades[i],"----->", metrosTotales[i],"m" )
    
def expPromedio(lista):
    promedio = 0
    for i in range(len(lista)):
        promedio = promedio + lista[i]
        promedioFull = promedio / len(lista)
    return promedioFull

    
def calculoExp():
    precioMetro = int(input("Ingresar precio por metro: "))
    for i in range(len(metrosTotales)):
        totalDpto = precioMetro * metrosTotales[i]
        expensas.append(totalDpto)
    for i in range(len(metrosTotales)):
        print("Unidad: ",unidades[i],"----paga-->",expensas[i])
    promedioTotal = expPromedio(expensas)
    print("El precio promedio de expensas es de: $",promedioTotal)
    
    
ingresoDatos()
calculoExp()

# --------------------------------------

# simulacro ej 1

socios = []
anios = []
cadete = 500
mayor = 1000
vitalicio = 50

def ingresoDatos():
    socio =""
    while socio != "f":
        socio = input("Ingrese C, M, o V .Para finalizar ingrese f ")
        if socio != "f":
            anio = int(input("Ingrese el anio de alta "))
            if (socio == "C" or socio == "M" or socio == "V") and (anio >= 1970):
                socios.append(socio)
                anios.append(anio)
            else:
                print("error ingresar de nuevo ")
    print(socios, anios)
    
def calcAn(anio):
   antiguedad = 2023 - anio
   return antiguedad

def sumaTotal(arr1, arr2, arr3):
    total = arr1 + arr2 + arr3 
    return total

def sumaCat(arr, cuota):
    total = len(arr) * cuota
    return total
    
def calculo():
    cadetes = []
    mayores = []
    vitaliciosFree = []
    vitalicios = []
    for i in range(len(socios)):
        if socios[i] == "C":
            cadetes.append(socios[i])
            
        if socios[i] == "M":
            mayores.append(socios[i])
        
        if socios[i] == "V" and (calcAn(anios[i]) > 30):
            vitaliciosFree.append(socios[i])
        
        if socios[i] == "V" and (calcAn(anios[i]) < 30):
            vitalicios.append(socios[i])
    print("cadetes ----> ", cadetes,"mayores ----> ", mayores, "vitalicios ----> ", vitalicios, "vitaliciosFree ----> ",vitaliciosFree)
    
    totalCadetes = sumaCat(cadetes, cadete)
    totalMayores = sumaCat(mayores, mayor)
    totalVitalicios = sumaCat(vitalicios, vitalicio)
    
    recaudacion = sumaTotal(totalCadetes, totalMayores, totalVitalicios)
    print("Recaudacion total: $", recaudacion)
    

ingresoDatos()
calculo()

# --------------------------------------------