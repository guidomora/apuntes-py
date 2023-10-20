# Funciones

# def creandoLaFuncion(animal):
#     if animal == "perro":
#         print("guauu guau")
#     elif animal == "gato":
#         print("miauu")
#     else:
#         print("no lo se")

# creandoLaFuncion("gato")

# Funcion que retorna valores

def crearPassword(nombre,numero):
    abc = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m"]
    multiplicacion = numero * len(nombre) - 4
    for letra in abc:
        if nombre[0] != letra :
            break
    masString = str(multiplicacion) + letra
    return masString

password = crearPassword('agus', 22)
print(f"tu password nueva es {password}")