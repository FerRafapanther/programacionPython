# -*- coding: utf-8 -*-
"""
Created on Wed May 21 17:18:27 2025

@author: Rocket
"""
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano

from MenuSecundario import *
from CuentaDebito import *
from CuentaCredito import *
from CuentaNomina import *

class MenuPrincipal:
    def __init__(self, mensaje):
        self.__mensajeBienvenida = mensaje

    def darBienvenida(self):
        print(self.__mensajeBienvenida)

    def menuCuentas(self):
        print("\nSelecciona la cuenta en la cual deseas trabajar:")

        while True:
            print("\n1. Débito")
            print("2. Crédito")
            print("3. Nómina")
            print("4. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")
            
            if opcion == "1":
                cuenta = CuentaDebito(450, "Fernando")
                MenuSecundario(cuenta).realizarOperacion()
            elif opcion == "2":
                cuenta = CuentaCredito(200, "Fernando")
                MenuSecundario(cuenta).realizarOperacion()
            elif opcion == "3":
                cuenta = CuentaNomina(340, "Fernando")
                MenuSecundario(cuenta).realizarOperacion()
            elif opcion == "4":
                print("Saliendo del sistema. ¡Gracias por utilizar Banxico!")
                break
            else:
                print("Opción no válida, intente de nuevo.")