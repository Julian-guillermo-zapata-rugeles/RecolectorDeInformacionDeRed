import os

def obtenerEstadoTarjetaRed():
    # Este módulo retorna información sobre el estado de red (tajeta)
    # además muestra la red conectada
    comando_busqueda = "nmcli | head -n 1"
    salida = os.popen(comando_busqueda).read().replace("\n","")
    return salida
