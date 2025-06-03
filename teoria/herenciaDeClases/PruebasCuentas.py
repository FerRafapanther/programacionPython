# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:50:38 2025

@author: Rocket
"""
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano

from MenuPrincipal import *
from MenuSecundario import *
from CuentaDebito import *
from CuentaCredito import *
from CuentaNomina import *


class PruebasCuentas:
    def __init__(self):
        self.menu_principal = MenuPrincipal("Bienvenido a Banxico.")

    def iniciar(self):
        self.menu_principal.darBienvenida()
        self.menu_principal.menuCuentas()


if __name__ == "__main__":
    pruebas = PruebasCuentas()
    pruebas.iniciar()
