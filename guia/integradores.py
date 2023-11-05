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