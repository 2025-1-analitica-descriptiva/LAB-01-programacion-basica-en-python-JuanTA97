"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_02():

    list = []
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for i in f:
            i = i.split("\t")
            list.append((i[0], 1))
    list = sorted(list)

    #reducer
    
    def reducer(list):
        result =[]
        for key, group in groupby(list, lambda x: x[0]):
            result.append((key, sum(value for _, value in group)))
        return result
    return reducer(list)



pregunta_02()

"""
Retorne la cantidad de registros por cada letra de la primera columna como
la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""
