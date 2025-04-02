# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:37:01 2025

@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

class Menu:
    def __init__(self, mensaje, cuenta):
        self.__mensajeBienvenida = mensaje
        self.__cuenta = cuenta
        
    def darBienvenida(self):
        print(self.__mensajeBienvenida)

    def OpcionRetirar(self):
        print("Usted seleccionó la opción retirar.")
        cantidad = float(input('Cantidad que desea retirar:: '))
        
        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        else:
            mensaje_retiro = self.__cuenta.retirar(cantidad)
            print(mensaje_retiro)
            print(f"Saldo después del retiro: {self.__cuenta.get_saldo()}")
            
    def OpcionDepositar(self):
        print("Usted seleccionó la opción depositar.")
        cantidad = float(input('Cantidad que desea depositar:: '))
        
        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        else:
            mensaje_deposito = self.__cuenta.depositar(cantidad)
            print(mensaje_deposito)
            print(f"Saldo después del depósito: {self.__cuenta.get_saldo()}") 
            
    def OpcionSalir(self):
        print("Usted seleccionó la opción salir.")
        
    def desplegarOpciones(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Retirar")
            print("2. Depositar")
            print("3. Salir")
            
            opcion = input("Ingrese el número de la opción deseada: ")
            
            if opcion == '1':
                self.OpcionRetirar()
            elif opcion == '2':
                self.OpcionDepositar()
            elif opcion == '3':
                self.OpcionSalir()
                break
            else:
                print("Opción no válida, intente de nuevo.")
            
           
                
            
        

            
            
            
    

    
    
        

        
        
        
        