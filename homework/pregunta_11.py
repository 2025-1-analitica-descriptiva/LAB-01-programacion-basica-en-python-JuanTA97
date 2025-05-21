"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():

    diccionario = {}
    combinado = []
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("\t")
            key = line[3].split(",")
            value = line[1]
            
            combinado.append(list(zip(key, value*len(key))))
    
    combinado = [item for sublista in combinado for item in sublista]
    diccionario = {}
    for elemento in sorted(combinado):
        if elemento[0] not in diccionario:
            diccionario[elemento[0]] = []
            diccionario[elemento[0]].append(int(elemento[1]))
        else:
            diccionario[elemento[0]].append(int(elemento[1]))

    return {k: sum(v) for k, v in diccionario.items()}
    
    
pregunta_11()

"""
Retorne un diccionario que contengan la suma de la columna 2 para cada
letra de la columna 4, ordenadas alfabeticamente.

Rta/
{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


"""
