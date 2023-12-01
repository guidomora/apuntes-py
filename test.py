# def burbujeo(lista):
#     for i in range(len(lista) -1):
#         for j in range(len(lista) -1-i):
#             if lista[j] > lista[j+1]:
#                 aux = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = aux







productos = []
precios = []

while len(productos) < 4:
    producto = int(input("Ingrese un producto: "))
    precio = int(input("Ingrese un precio: "))
    if producto > 99 and precio > 0:
        productos.append(producto)
        precios.append(precio)
    else :
        print("nooo")
    
print(productos) 