frutas = ["manzana", "frutilla", "banana", "durazno", "kiwi"]

# cada vez que la fruta sea frutilla se saltea y sigue iterando
# for fruta in frutas:
#     if fruta == "frutilla":
#         continue
#     print(fruta)
    
# cuando sea igual a durazno se termina el bucle
# despues de un break no se ejecta nada de lo que haya despues 
for fruta in frutas:
    print(fruta)
    if fruta == "durazno":
        break
print("terminado")