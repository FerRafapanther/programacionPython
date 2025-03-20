# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:05:28 2025

@author: Rocket
"""
# Fecha: Marzo, 2025
# @version: 1.3
# @autor: FernandoRafaelLopezSolano

from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuenta = cuenta
        
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_edad(self):
        return self.__edad
 
    def get_cuenta(self):
        return self.__cuenta
        
    def imprimirDetalles(self):
        print("nombre::", self.__nombre)
        print("direccion::", self.__direccion)
        print("edad::", self.__edad)
        print("Detalles de la cuenta:")
        self.__cuenta.imprimirDetalles()
        
        

         
        
        
    
