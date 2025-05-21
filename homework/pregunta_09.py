"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_09():

    lista = []

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("\t")[4].split(",")
            line = [item.split(":")[0] for item in line]
            lista.append(line)
    
    lista = [item for sublista in lista for item in sublista]
    final = []
    for i in sorted(lista):
        final.append((i, 1))

    result = {}
    for key, group in groupby(final, lambda x: x[0]):
        result[key] = sum(value for _, value in group)
    return result
    #print(final)
pregunta_09()

"""
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
