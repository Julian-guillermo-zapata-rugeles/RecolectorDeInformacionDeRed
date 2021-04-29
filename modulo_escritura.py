import os
import time


def crearCarpeta():
    #creacion de la carpeta analiticas
    os.system("mkdir ANALITICAS 2>/dev/null")


def escribirArchivo(lista_elementos):
    # se almacenará la información necesaria en el archivo analiticas que se encuentre presente
    crearCarpeta()

    salida = str(len(lista_elementos))+";"  # ESCRITURA DE NUMERO DE CONECTADOS (ENTERA)
    salida = salida + str(time.localtime()[0:5]).replace(" ","").replace(",","/")+";" # FECHA Y HORA DEL SISTEMA
    salida = salida +"/".join(lista_elementos) # IP DE LOS DISPOSITIVOS
    

    print(salida)
