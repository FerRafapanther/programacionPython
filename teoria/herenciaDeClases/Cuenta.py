# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:43:38 2025

@author: Equipo 34
"""

class Cuenta:
    
    def __init__(self, valor, propietario):
        self.__saldo= valor
        self.__propietario= propietario
        
        
    def imprimirDetalles (self):
        
        print("saldo::", self.__saldo)
        print("nombre::", self.__propietario)
        
    def retirar (self,cantidad):
        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        
        elif cantidad > self.__saldo:
            return "Error: Fondos insuficientes."
        
        else:
            self.__saldo = self.__saldo - cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            
    def depositar (self,cantidad):
        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        else:
            self.__saldo = self.__saldo + cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
    
    def __str__(self):
        return "Tipo: " + str(self.__tipo) + "\nSaldo: " + str(self.__saldo)

    