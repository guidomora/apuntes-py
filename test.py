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
