# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:12:37 2025

@author: Rocket
"""
# Fecha: Febrero, 2025
# @version: 1.1
# @autor: FernandoRafaelLopezSolano

class Cuenta:
    def __init__(self, valor, tipo, propietario):
        self.saldo=valor
        self.tipo=tipo
        self.propietario=propietario
        
    def imprimirDetalles (self):
        print("saldo::", self.saldo)
        print("tipo::", self.tipo)
        print("nombre::", self.propietario)
        
    def retirar (self,cantidad):
        self.saldo=self.saldo-cantidad
        
    def depositar (self,cantidad):
        self.saldo=self.saldo+cantidad
        
        
    
        
