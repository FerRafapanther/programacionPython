# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:20:41 2025

@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

from Menu import *
from Cliente import *
from Cuenta import *

# Crear cuentas
cuenta1 = Cuenta(12400, "debito")
cuenta2 = Cuenta(15000, "credito")
cuenta3 = Cuenta(8740, "nomina")


cliente = Cliente("Fernando", "Tacubaya 10", 19, [cuenta1, cuenta2, cuenta3])

menu = Menu("Bienvenido al Banco!", cliente)

menu.darBienvenida()

menu.menuDeCuentas()





