legajos = []
calificaciones= []

def ingresarDatos():
    total = 0
    legajo = 0
    aprobados = 0
    desaprobados = 0
    while legajo != -1:
        legajo = int(input("Ingresar su numero de legajo: "))
        if legajo != -1:
            legajos.append(legajo)   
    
    while len(calificaciones) != len(legajos):
        nota = -1
        while nota < 1 or nota > 10:
            nota = int(input("Ingresar la nota para el legajo: "))
            total += nota
        calificaciones.append(nota)

    for i in range(len(calificaciones)):
        promedio = total / len(calificaciones)
        if calificaciones[i] >= 4:
            aprobados += 1
        elif calificaciones[i] < 4:
            desaprobados += 1
    print("Promedio: ", promedio,
          "Aprobados: ", aprobados,
          "Desaprobados: ", desaprobados)
            
                              


ingresarDatos()
print("Legajos: ", legajos)
print("Calificaciones: ", calificaciones)    

# -------------------------------------------------

nroUnidad = []
mCuadrado = []
expensas = []

def ingresarUnidades():
    for i in range(0, 5):
        unidad = input("Unidad: ")
        while len(nroUnidad) > 0 and nroUnidad[-1] == unidad:
            print("Ya ingreso esa unidad")
            unidad = input("Ingrese una unidad diferente: ")
        nroUnidad.append(unidad)


def ingresarMetros():
    for i in range(len(nroUnidad)):
        metros = int(input("Metros: "))
        mCuadrado.append(metros)
        
        
def calculoExpensas():
    precioPorMetro = 2000
    for i in range(len(mCuadrado)):
        expensa = mCuadrado[i] * precioPorMetro
        expensas.append(expensa)

def calculoPromedio():
    total = 0
    for i in range(len(expensas)):
        total = total + expensas[i]
    promedio = total / len(expensas)
    print("Valor de expensa Promedio :" ,promedio)
    return promedio

ingresarUnidades()
ingresarMetros()
calculoExpensas()
print(
    "Unidades: ",nroUnidad,
    "Metros: ",mCuadrado,
    "Expensas: ", expensas
)
calculoPromedio()
    