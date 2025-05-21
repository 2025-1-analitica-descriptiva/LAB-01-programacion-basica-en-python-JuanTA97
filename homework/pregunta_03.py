"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_03():

    list = []
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for i in f:
            i = i.split("\t")
            list.append((i[0], int(i[1])))
    list = sorted(list)
    print(list)

    #reducer
    def reducer(list):
        result =[]
        for key, group in groupby(list, lambda x: x[0]):
            result.append((key, sum(value for _, value in group)))
        return result
    return reducer(list)

pregunta_03()  
"""
Retorne la suma de la columna 2 por cada letra de la primera columna como
una lista de tuplas (letra, suma) ordendas alfabeticamente.

Rta/
[('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

"""
