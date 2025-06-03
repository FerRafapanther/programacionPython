# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:25:42 2025

@author: Rocket
"""
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano

class Cuenta:
    def __init__(self, saldo, propietario):
        self.__saldo = saldo
        self.__propietario = propietario
    
    def imprimirDetalles(self):
        print(f"Saldo: {self.__saldo}")
        print(f"Propietario: {self.__propietario}")
    
    def retirar(self, cantidad):
        if cantidad < 0:
            return "Error: La cantidad ingresada no puede ser negativa."
        elif cantidad > self.__saldo:
            return "Error: Fondos insuficientes."
        else:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"

    def depositar(self, cantidad):
        if cantidad < 0:
            return "Error: La cantidad ingresada no puede ser negativa."
        self.__saldo += cantidad
        return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"

    def __str__(self):
        return f"Saldo: {self.__saldo}\nPropietario: {self.__propietario}"

    