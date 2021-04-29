import os
import modulo_menu




def ping(ip_probe):
    # esta función permite obtener dos posibles estados de un dispositivo
    # 1 si está activo
    # 0 en caso contrario/ no existencia


    comando_busqueda = "ping -c 1 -W 1 " + str(ip_probe) + " | grep \"received\" | awk {'print $4'}"
    #print(comando_busqueda) # descomentar para obtener información del comando y su visualización.
    resultado_busqueda = os.popen(comando_busqueda).read().replace("\n","").replace(" ","")
    if len(resultado_busqueda)==0:
        resultado_busqueda=False
    #print(resultado_busqueda)
    return resultado_busqueda








def BusquedaPorRango(ip_start,ip_finish):
    # esta función recibe dos rangos de busqueda
    # solo se alternan los ultimos rangos para dicha función 192.168.1.X
    # modifique a su conveniencia.

    print("[buscando mediante rango]\nTiempo : {} segundos (aproximadamente) ".format(ip_finish-ip_start))
    IP_BASE = "192.168.1." # + [ip_start/ip_finish]
    lista_activos = []
    for iterador in range( ip_start, ip_finish + 1):
        # -------- llamamos a ping() para obtener 0 o 1
        ip_de_prueba=  IP_BASE + str(iterador)
        respuesta = ping(ip_de_prueba)
        if(respuesta=="1"):
            # añadimos al diccionario
            lista_activos.append(ip_de_prueba)

    for actives in  lista_activos:
        print(actives)
    return lista_activos
