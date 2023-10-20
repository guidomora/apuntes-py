# For:

animales = ["perro", "gato", "loro", "condor"]
# for hola in animales:
#     print(f"el animal ahora es: {hola}")


# For con 2 arrays
# animales = ["perro", "gato", "loro", "condor"]
# numeros = [1, 2, 3, 4]

# for numero, animal in zip(animales, numeros):
#     print(f"recorriendo numeros: {numero}")
#     print(f"recorriendo animales: {animal}")

#For range
# ejecuta el ciclo segun el rango que le pongamos en este caso del 5 al 15
# si solo le pasamos un parametro solo va a ser del 0 a ese numero
# for numero in range(5, 15):
#     print(numero)


#For enumerate ---> es la forma correcta de recorrer un array
# nos devuelve cada elemento del array con su propio indice
# for animal in enumerate(animales):
#     print(animal)
    
    
    
    
# For con else
# else siemre se ejecuta al final del bucle y sin importar si el array esta vacio o lo que fuese 
# for animal in animales:
#     print(animal)
# else:
#     print("Termino el bucle")


# Iterando diccionarios con for

diccionario = {
    "nombre":"guido",
    "apellido": "morabito",
    "edad":23
}

# for key in diccionario.items():
#     print(key)

for dato in diccionario.items():
    key = dato[0]
    valor = dato[1]
    print(f"key: {key} valor -->{valor}")