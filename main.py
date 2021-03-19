texto = """este es un texto el cual deben contar el numero
de palabras que tiene, deben tener en cuenta,
que algunas palabras se separa por un punto, y una
coma, tambien hay que tener en cuenta, que las palabras
escritas EN MAYUSCULAS y minusculas cuenta como una este. Texto"""

quitar = ",;:.\n!\"'"
for caracter in quitar:
    texto = texto.replace(caracter,
                          "")

texto=texto.lower()
palabras = texto.split(" ")

diccionario_frecuencia = {}

for palabra in palabras:
        if palabra in diccionario_frecuencia:
                diccionario_frecuencia[palabra] += 1
        else:
                diccionario_frecuencia[palabra] = 1

for palabra in diccionario_frecuencia:
        frecuencia = diccionario_frecuencia[palabra]
        print(f"La palabra '{palabra}' se repite {frecuencia}")