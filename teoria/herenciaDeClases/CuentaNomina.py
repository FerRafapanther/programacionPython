# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:33:20 2025

@author: Rocket
"""
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano

from Cuenta import*

class CuentaNomina(Cuenta):
    def __init__(self, saldo, propietario):
        Cuenta.__init__(self, saldo, propietario)
        self.__tipo = "Nomina"
        
    def __str__(self):
        return f"Tipo: {self.__tipo}\n{Cuenta.__str__(self)}"
    