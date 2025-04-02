# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:05:28 2025

@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad, cuentas=None):
        if cuentas is None:
            cuentas = []  
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.cuentas = cuentas 
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_edad(self):
        return self.__edad

    def imprimirDetalles(self):
        print("nombre::", self.__nombre)
        print("direccion::", self.__direccion)
        print("edad::", self.__edad)
        print("Detalles de las cuentas:")
        for cuenta in self.cuentas:
            cuenta.imprimirDetalles()

    def __str__(self):
        cuentas_str = "\n".join(str(cuenta) for cuenta in self.cuentas)  
        return f"nombre::{self.__nombre}\ndireccion::{self.__direccion}\nedad::{self.__edad}\n{cuentas_str}"

    def agregarCuenta(self, cuenta):
        if isinstance(cuenta, Cuenta):  
            self.cuentas.append(cuenta)
        else:
            print("Error: El objeto no es una instancia de la clase Cuenta.")
    
    def eliminarCuenta(self, indice):
        if 0 <= indice < len(self.cuentas):
            self.cuentas.pop(indice)  
        else:
            print("Error: Índice inválido.")
    
    def infoCuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)  
        
        

         
        
        
    