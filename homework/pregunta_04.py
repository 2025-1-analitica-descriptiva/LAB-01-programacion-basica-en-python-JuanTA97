"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_04():

    list = []
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for i in f:
            i = i.split("\t")
            list.append((i[2].split("-")[1], 1))
    list = sorted(list)

    #reducer

    def reducer(list):
        result =[]
        for key, group in groupby(list, lambda x: x[0]):
            result.append((key, sum(value for _, value in group)))
        return result
    return reducer(list)

pregunta_04()
"""
La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
cantidad de registros por cada mes, tal como se muestra a continuación.

Rta/
[('01', 3),
 ('02', 4),
 ('03', 2),
 ('04', 4),
 ('05', 3),
 ('06', 3),
 ('07', 5),
 ('08', 6),
 ('09', 3),
 ('10', 2),
 ('11', 2),
 ('12', 3)]

"""
