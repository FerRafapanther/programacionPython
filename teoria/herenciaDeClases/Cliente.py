# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:41:59 2025

@author: Equipo 34
"""

class Cliente:
    
    def __init__(self, nombre, direccion, edad, cuenta):
        
        self.__nombre=nombre
        self.__direccion=direccion
        self.__edad=edad
        self.__cuenta=cuenta
        
        
    def imprimirDetalles (self):
        
        print("nombre::", self.__nombre)
        print("direccion::", self.__direccion)
        print("edad::", self.__edad)
        print("Detalles de la cuenta:")
        self.__cuenta.imprimirDetalles()
        
        
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
      
        