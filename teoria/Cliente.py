# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:05:28 2025

@author: Rocket
"""
# Fecha: Febrero, 2025
# @version: 1.0
# @autor: FernandoRafaelLopezSolano

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre=nombre
        self.direccion=direccion
        self.edad=edad
        
    def imprimirDetalles (self):
        print("Desde el metodo")
        print("nombre::", self.nombre)
        print("direccion::", self.direccion)
        print("edad::", self.edad)
        

         
        
        
    