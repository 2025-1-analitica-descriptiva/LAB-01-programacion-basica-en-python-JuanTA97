"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    
    list=[]
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for i in f:
            i =i.split("\t")
            list.append(int(i[1]))
    #print(list)
    return sum(list)
    

         
        # 
        # print(list(f))

pregunta_01()
    
"""
Retorne la suma de la segunda columna.

Rta/
214

"""
