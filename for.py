# For:

# animales = ["perro", "gato", "loro", "condor"]
# for hola in animales:
#     print(f"el animal ahora es: {hola}")


# For con 2 arrays
animales = ["perro", "gato", "loro", "condor"]
numeros = [1, 2, 3, 4]

for numero, animal in zip(animales, numeros):
    print(f"recorriendo numeros: {numero}")
    print(f"recorriendo animales: {animal}")