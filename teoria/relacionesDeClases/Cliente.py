# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:05:28 2025

@author: Rocket
"""
# Fecha: Marzo, 2025
# @version: 1.2
# @autor: FernandoRafaelLopezSolano

from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre=nombre
        self.direccion=direccion
        self.edad=edad
        self.cuenta=cuenta
        
        
    def imprimirDetalles (self):
        print("nombre::", self.nombre)
        print("direccion::", self.direccion)
        print("edad::", self.edad)
        print("Detalles de la cuenta")
        self.cuenta.imprimirDetalles()
        
        

         
        
        
    