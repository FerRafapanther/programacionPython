# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:05:28 2025

@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, direccion, edad, cuentas=None):
        if cuentas is None:
            cuentas = []  
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.cuentas = cuentas  

        for cuenta in cuentas:
            if isinstance(cuenta, Cuenta):
                self.cuentas.append(cuenta)
            else:
                print(f"Advertencia: La cuenta {cuenta} no es válida y no se ha agregado.")
    
    def getnombre(self):
        return self.__nombre
    
    def getdireccion(self):
        return self.__direccion
    
    def getedad(self):
        return self.__edad

    def imprimirDetalles(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Dirección: {self.__direccion}")
        print(f"Edad: {self.__edad}")
        print("Detalles de las cuentas:")
        for cuenta in self.cuentas:
            cuenta.imprimirDetalles()

    def __str__(self):
        cuentas_str = "\n".join(str(cuenta) for cuenta in self.cuentas)  
        return f"Nombre: {self.__nombre}\nDirección: {self.__direccion}\nEdad: {self.__edad}\n{cuentas_str}"

    def agregarCuenta(self, cuenta):
        if isinstance(cuenta, Cuenta):
            self.cuentas.append(cuenta)
        else:
            raise TypeError("El objeto no es una instancia de la clase Cuenta.")
            
    def eliminarCuenta(self, indice):
        if 0 <= indice < len(self.cuentas):
            cuenta_eliminada = self.cuentas.pop(indice)  
            print(f"Cuenta eliminada: {cuenta_eliminada}")
        else:
            print("Error: Índice inválido.")
    
    def infoCuentas(self):
        if not self.cuentas:
            print("El cliente no tiene cuentas asociadas.")
        else:
            for cuenta in self.cuentas:
                cuenta.imprimirDetalles()

    
        

         
        
        
    