
import os

def obtenerVelocidad():
    #
    # Este módulo permite obtener la velocidad actual de la red
    # Necesita del modulo speed-test-cli para ejecutarse correctamente
    # el return de este módulo será una cadena con la velocidad de la red
    # medida por el dispositivo en dicho momento
    # deberá retornar ( x ,  x   , x ) ping , bajada , subida
    # deberá retornar ( 0  , 0   , 0 ) si falla la red para dicho caso

    comando_busqueda  = "speedtest --simple --timeout 3 2>/dev/null"
    salida = os.popen(comando_busqueda).read()
    lista_salida = salida.split("\n")
    lista_final = []
    for i  in lista_salida:
        if len(i)!=0:
            lista_final.append(i)

    if len(lista_final)==0:
        salida = "(0,0,0)"
    else:
        salida = "(" + ",".join(lista_final) + ")"
    print("+++++++++++++++ RESULTADOS DE RED +++++++++++++++")
    print(salida)
    return salida
