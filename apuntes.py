# Aplicacion de los metodos
# hola = "asd,asd,ooo"
# print(hola.split(","))

# String Methods
# --- .upper
# --- .lower
# --- .capitalize
# --- .dir
# --- .find busca lo que le pasemos como argumento y nos devuelve la posicion, si no encuentra
#       nos devuelve -1
# --- .index igual que find pero si no encuentra nos da error
# --- .isnumeric si es numerico devuelve true sea string o numero
# --- .isalpha si es alfanumerico devuelve true a-z el espacio no cuenta y da false
# --- .count devuelve la cantidad de veces que coincida ej cuantas veces
#       encuentra la letra d
# --- .len -------> length de js :)
# --- .endswith  termina con... da true
# --- .startswith empieza con... da true
# --- .replace reemplaza un pedazo del string por lo que le demos 
#       print(hola.replace("d", "reemplazamos")) ----> asreemplazamosasreemplazamos
# --- .split separa con el string que le pasemos y retorna un array
#       print(hola.split(",")) ----> ['asd', 'asd', 'ooo'] 

# Array Methods
lista = list(["asdasd","asdasd", "asdasd"])
print(len(lista))

# --- .len ---> js :)  print(len(lista))
# --- .append lista.append("asdas","eeee") agrega al final
# --- .insert inserta en la posicion que le indiquemos lista.insert(2, "hola")
# --- .extend agrega varios elementos a la lista le pasamos un array pero, lo
#       agrega separado ----> lista.extend(["hola", "chau"])
# --- .pop elimima un elemento segun la posicion que le pasemos .pop(4)
# --- .remove elimina el parametro que le pasemos .remove("asdasd")