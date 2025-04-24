# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:20:04 2025

@author: Equipo 34
"""

from Cuenta import *

class CuentaHija(Cuenta):
    def __init__(self,saldo,tipo):
        
        Cuenta.__init__(self, valor, propietario)
        self.__tipo=tipo
        
    