# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:12:37 2025

@author: Rocket
"""
# Fecha: Marzo, 2025
# @version: 1.3
# @autor: FernandoRafaelLopezSolano

class Cuenta:
    def __init__(self, valor, tipo, propietario):
        self.__saldo = valor
        self.__tipo = tipo
        self.__propietario = propietario
        
    def imprimirDetalles(self):
        print("saldo::", self.__saldo)
        print("tipo::", self.__tipo)
        print("nombre::", self.__propietario)
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("Error: El saldo no puede ser negativo.")
    
    def retirar(self, cantidad):
        if cantidad < 0:
            return "Error: La cantidad a retirar no puede ser negativa."
        elif cantidad > self.__saldo:
            return "Error: Fondos insuficientes."
        else:
            self.__saldo -= cantidad
            return "Retiro exitoso."
        
    def depositar(self, cantidad):
        if cantidad < 0:
            return "Error: La cantidad a depositar no puede ser negativa."
        else:
            self.__saldo += cantidad
            return "Depósito exitoso."
            
    
        
        
        
        
    
        
