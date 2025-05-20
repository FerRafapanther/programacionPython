# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:28:01 2025

@author: Rocket
"""

class Menu:
    def __init__(self, mensaje, cuentas=None):
        self.__mensajeBienvenida = mensaje
        self.__cuentas = cuentas if cuentas is not None else []

    def darBienvenida(self):
        print(self.__mensajeBienvenida)

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

    # Método para seleccionar cuenta
    def menuCuentas(self):
        print("\nSelecciona la cuenta en la cual deseas trabajar:")

        while True:
            print("\n1. Débito")
            print("2. Crédito")
            print("3. Nómina")
            print("4. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.__cuenta = CuentaDebito(450, "Fernando")  # Selección de Cuenta Débito
                self.realizarOperacion()
            elif opcion == "2":
                self.__cuenta = CuentaCredito(200, "Fernando")  # Selección de Cuenta Crédito
                self.realizarOperacion()
            elif opcion == "3":
                self.__cuenta = CuentaNomina(340, "Fernando")  # Selección de Cuenta Nómina
                self.realizarOperacion()
            elif opcion == "4":
                print("Saliendo del menú de cuentas.")
                break
            else:
                print("Opción no válida, intente de nuevo.")

    # Método para elegir operación
    def realizarOperacion(self):
        tipo_cuenta = self.__cuenta.__class__.__name__  # Obtiene el nombre de la clase
        print(f"\nUsted seleccionó la cuenta de tipo {tipo_cuenta}")
        print("¿Qué operación desea realizar?")

        while True:
            print("\n1. Retirar")
            print("2. Depositar")
            print("3. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.opcionRetirar()
            elif opcion == "2":
                self.opcionDepositar()
            elif opcion == "3":
                print("Usted seleccionó la opción salir de operaciones.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
    