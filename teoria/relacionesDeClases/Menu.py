# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:37:01 2025

@author: Rocket
"""
# Fecha: Marzo, 2025
# @version: 1.2
# @autor: FernandoRafaelLopezSolano

class Menu:
    def __init__(self, mensaje):
        self.mensajeBienvenida= mensaje
        
    def darBienvenida(self):
        print(self.mensajeBienvenida)
        
    def OpcionRetirar(self):
        print("Usted seleccionó la opción retirar.")
        
    def OpcionDepositar(self):
        print("Usted seleccionó la opción depositar.")
        
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
                
            
        

            
            
            
    

    
    
        

        
        
        
        