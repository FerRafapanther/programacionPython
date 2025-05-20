# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:31:32 2025

@author: Rocket
"""
from Cuenta import *

class CuentaCredito(Cuenta):
    def __init__(self, saldo, propietario):
        Cuenta.__init__(self, saldo, propietario)  # ← Esta línea estaba con ":" al final (eso es un error)
        self.__tipo = "Credito"

    def __str__(self):
        return f"Tipo: {self.__tipo}\n{Cuenta.__str__(self)}"