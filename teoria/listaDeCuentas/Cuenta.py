# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:12:37 2025

@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

class Cuenta:
    
    tiposDeCuenta = ['credito', 'debito', 'nomina']
    
    def __init__(self, valor, tipo):
        if tipo not in Cuenta.tiposDeCuenta:
            raise ValueError(f"Tipo de cuenta no válido. Debe ser uno de: {', '.join(Cuenta.tiposDeCuenta)}")
        self.__saldo = valor
        self.__tipo = tipo
        
    def imprimirDetalles(self):
        print("saldo::", self.__saldo)
        print("tipo::", self.__tipo)
        
    def getSaldo(self):
        return self.__saldo
    
    def getTipo(self):
        return self.__tipo
    
    def setSaldo(self, nuevo_saldo):
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
            return f"Retiro exitoso. Saldo actual: {self.__saldo}"
        
    def depositar(self, cantidad):
        if cantidad < 0:
            return "Error: La cantidad a depositar no puede ser negativa."
        else:
            self.__saldo += cantidad
            return f"Depósito exitoso. Saldo actual: {self.__saldo}"
    
    def __str__(self):
        return "Tipo: " + str(self.__tipo) + "\nSaldo: " + str(self.__saldo)

        
    



    
        
        
        
        
    
        