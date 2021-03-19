filename = 'textoAqui.txt'


try:
    with open(filename) as f_obj:
            contens = f_obj.read()
            print(contens)
except FileNotFoundError:
        msg = "Archivo " + filename + " no existe"
        print( msg )

else:
    words = contens.split(" ")
    diccionario = dict()

    for p in words:
            diccionario[p] = diccionario.get(p, 0) + 1
            print(diccionario[p])
   # print(diccionario)