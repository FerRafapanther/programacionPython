# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:44:44 2025

@author: Equipo 34
"""

class Menu:
    
    def __init__(self, mensaje, cuenta):
        
        self.__mensajeBienvenida= mensaje
        self.__cuenta= cuenta
        
        
    def darBienvenida(self):
        print(self.__mensajeBienvenida)
        
    
    def realizarOperacion(self):
        tipo_cuenta = self.__cuenta.getTipo()  
        print(f"Usted seleccionó cuenta de {tipo_cuenta}")
        print("Selecciona la operación que desea realizar")

        while True:
            print("\nSeleccione una opción:")
            print("1. Retirar")
            print("2. Depositar")
            print("3. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.opcionRetirar()
            elif opcion == '2':
                self.opcionDepositar()
            elif opcion == '3':
                print("Usted seleccionó la opción salir.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        
    def menuCuentas(self):
        menuDeCuentas(self):
        print("Selecciona la cuenta en la cual deseas trabajar")
        
        while True:
            print("1. Crédito")
            print("2. Débito")
            print("3. Nómina")
            print("4. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.realizarOperacion()  
            elif opcion == "2":
                self.realizarOperacion()  
            elif opcion == "3":
                self.realizarOperacion()  
            elif opcion == "4":
                print("Saliendo del menú de cuentas.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        
    
    def opcionRetirar(self):
        print("Usted seleccionó la opción retirar.")
        
        cantidad = float(input('Cantidad que desea retirar:: '))
        
        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
            
        else:
            mensaje_retiro = self.__cuenta.retirar(cantidad)
            print(mensaje_retiro)
            print(f"Saldo después del retiro: {self.__cuenta._Cuenta__saldo}")
            
    def OpcionDepositar(self):
        print("Usted seleccionó la opción depositar.")
        cantidad = float(input('Cantidad que desea depositar:: '))
        
        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        else:
            mensaje_deposito = self.__cuenta.depositar(cantidad)
            print(mensaje_deposito)
            print(f"Saldo después del depósito: {self.__cuenta._Cuenta__saldo}")
            
            
            
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
            
    

   