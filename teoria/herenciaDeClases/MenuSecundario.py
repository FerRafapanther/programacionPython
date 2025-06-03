# -*- coding: utf-8 -*-
"""
Created on Wed May 21 17:18:46 2025

@author: Rocket
"""
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano

class MenuSecundario:
    def __init__(self, cuenta):
        self.__cuenta = cuenta

    def realizarOperacion(self):
        tipo_cuenta = self.__cuenta.__class__.__name__
        print(f"\nUsted seleccionó la cuenta de tipo {tipo_cuenta}")
        print("¿Qué operación desea realizar?")

        while True:
            print("\n1. Retirar")
            print("2. Depositar")
            print("3. Volver al menú principal")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.opcionRetirar()
            elif opcion == "2":
                self.opcionDepositar()
            elif opcion == "3":
                print("Volviendo al menú principal...Seleccione la cuenta en la que desea trabajar:")
                break
            else:
                print("Opción no válida, intente de nuevo.")

    def opcionRetirar(self):
        print("Usted seleccionó la opción retirar.")
        try:
            cantidad = float(input('Cantidad que desea retirar:: '))
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
            return

        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        else:
            mensaje_retiro = self.__cuenta.retirar(cantidad)
            print(mensaje_retiro)
            print(f"Saldo después del retiro: {self.__cuenta._Cuenta__saldo}")

    def opcionDepositar(self):
        print("Usted seleccionó la opción depositar.")
        try:
            cantidad = float(input('Cantidad que desea depositar:: '))
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
            return

        if cantidad < 0:
            print("Error: La cantidad ingresada no puede ser negativa. Intenta nuevamente.")
        else:
            mensaje_deposito = self.__cuenta.depositar(cantidad)
            print(mensaje_deposito)
            print(f"Saldo después del depósito: {self.__cuenta._Cuenta__saldo}")