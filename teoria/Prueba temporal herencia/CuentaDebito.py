# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:32:53 2025

@author: Rocket
"""
from Cuenta import*

class CuentaDebito(Cuenta):
    def __init__(self, saldo, propietario):
        Cuenta.__init__(self, saldo, propietario)  
        self.__tipo = "Debito"
    
    def __str__(self):
        return f"Tipo: {self.__tipo}\n{Cuenta.__str__(self)}"
