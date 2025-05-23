"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():

    diccionario = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("\t")
            key = line[0]
            value = line[4].split(",")
            value = [int(i.split(":")[1]) for i in value]
            value = sum(value)
            if key not in diccionario:
                diccionario[key] = value
            else:
                diccionario[key] += value

    return diccionario

pregunta_12()
"""
Genere un diccionario que contengan como clave la columna 1 y como valor
la suma de los valores de la columna 5 sobre todo el archivo.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

"""
