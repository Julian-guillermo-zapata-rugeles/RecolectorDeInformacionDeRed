import os
import time
import modulo_speed
import modulo_status

def crearCarpeta():
    #creacion de la carpeta analiticas
    os.system("mkdir ANALITICAS 2>/dev/null")


def escribirArchivoNormal(lista_elementos):
    """
    se almacenará la información necesaria en el archivo analiticas que se encuentre presente
    esta función escribirá de manera básica sin información adicional

    salida esperada =  numero_dispositivos ; hora_local ; dispositivos

    """
    crearCarpeta()
    salida = str(len(lista_elementos))+";"  # ESCRITURA DE NUMERO DE CONECTADOS (ENTERA)
    salida = salida + str(time.localtime()[0:5]).replace(" ","").replace(",","/")+";" # FECHA Y HORA DEL SISTEMA
    salida = salida +"/".join(lista_elementos) # IP DE LOS DISPOSITIVOS

    # UTILIZA TU SALIDA DE PREFERENCIA #
    archivo_salida =  open("ANALITICAS/analiticas.py","a")
    archivo_salida.write(salida)
    archivo_salida.write("\n")
    archivo_salida.close()







def escribirArchivoCompleto(lista_elementos):
    """
    se almacenará la información necesaria en el archivo analiticas que se encuentre presente
    esta función escribirá de manera básica sin información adicional

    salida esperada =  numero_dispositivos ; hora_local ; velocidad ; red_conectada ; dispositivos

    """
    crearCarpeta()
    # obtenemos la velocidad del internet en dicho momento
    velocidad_obtenida = modulo_speed.obtenerVelocidad()
    #print("vel : ",velocidad_obtenida)
    estado_tarjeta = modulo_status.obtenerEstadoTarjetaRed()

    salida = str(len(lista_elementos))+";"  # ESCRITURA DE NUMERO DE CONECTADOS (ENTERA)
    salida = salida + str(time.localtime()[0:5]).replace(" ","").replace(",","/")+";" # FECHA Y HORA DEL SISTEMA
    salida = salida + velocidad_obtenida + ";" # VELOCIDAD
    salida = salida + estado_tarjeta + ";"
    salida = salida +"/".join(lista_elementos) # IP DE LOS DISPOSITIVOS

    print(salida)
    # UTILIZA TU SALIDA DE PREFERENCIA #
    archivo_salida =  open("ANALITICAS/analiticas.py","a")
    archivo_salida.write(salida)
    archivo_salida.write("\n")
    archivo_salida.close()
