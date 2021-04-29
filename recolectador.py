import modulo_ping
import modulo_menu
import modulo_escritura



__author__ = "Julian Guillemo Zapata Rugeles"
__correo__ = "julianruggeles@gmail.com"
__descripcion__ = """

                    GNU GENERAL PUBLIC LICENSE
                     Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.



Este script tiene como objetivo recolectar información de red básica mediante ping
dichas analíticas se uniran además con las respectivas fechas de sondeo y velocidad
el objetivo principal es detectar la cantidad de dispositivos y su relación con la
velocidad de red de ese instante.

Este script se realizó para entornos de tipo GNU/LINUX
Fue testeado en debian buster 10

    Dependencias : python 3 +
    sudo apt-get install speedtest-cli (para el módulo de velocidad)


"""

dispositivo_activos = modulo_ping.BusquedaPorRango(20,30)
modulo_escritura.escribirArchivoCompleto(dispositivo_activos)
