# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:20:31 2025

@author: Equipo 34
"""
from Cuenta import *
from cuentaHija import *
from Cliente import *

class Pruebas:
    pass

cuenta1=Cuenta(3000, 'Jose')
print(cuenta1)

cuenta2.depositar(400)
print(cuenta2)

cuenta3= cuentaHija (200, 'Yolanda', 'debito')
print(cuenta3)

