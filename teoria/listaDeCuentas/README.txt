# Fecha: Febrero, 2025
# @version: 1.0
# @autor: FernandoRafaelLopezSolano

README MENU
En este archivo se encuentra la clase Menu con el artributo:
mensajeBienvenida

y se definio los 2 metodos:
def __init__
def darBienvenida

README CLIENTE
En este archivo se encuentra la clase Cliente con sus 3 atributos:
nombre
direccion
edad

y se definio los 2 metodos:
def __init__
def __imprimir detalles


README CUENTA
En este archivo se encuentra la clase Cuenta con sus 3 atributos:
saldo
tipo
propietario

y se definio los 4 metodos:
def __init__
def __imprimir detalles
def retirar
def depositar

REAME MAIN
En este archivo se encuentra la clase Main, aqui se realizan las pruebas de
los metodos de las clases:
Cliente
Cuenta
Menu




from Menu import *
from Cliente import *
from Cuenta import *

class Main:
    pass

cuenta1 = Cuenta(900, "credito")
cuenta2 = Cuenta(700, "debito")

# Crear un cliente con las cuentas
cliente = Cliente("Fernando", "Zaragora 08", 30, [cuenta1, cuenta2])

# Mostrar los detalles del cliente y sus cuentas
cliente.imprimirDetalles()

# Agregar una nueva cuenta
cuenta3 = Cuenta(1000, "nomina")
cliente.agregarCuenta(cuenta3)

# Mostrar nuevamente los detalles
print("\nDespués de agregar una nueva cuenta:")
cliente.imprimirDetalles()

# Eliminar una cuenta
cliente.eliminarCuenta(1)

# Mostrar después de eliminar una cuenta
print("\nDespués de eliminar una cuenta:")
cliente.imprimirDetalles()




from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad, cuentas=None):
        if cuentas is None:
            cuentas = []  
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.cuentas = cuentas 
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_edad(self):
        return self.__edad

    def imprimirDetalles(self):
        print("nombre::", self.__nombre)
        print("direccion::", self.__direccion)
        print("edad::", self.__edad)
        print("Detalles de las cuentas:")
        for cuenta in self.cuentas:
            cuenta.imprimirDetalles()

    def __str__(self):
        cuentas_str = "\n".join(str(cuenta) for cuenta in self.cuentas)  
        return f"nombre::{self.__nombre}\ndireccion::{self.__direccion}\nedad::{self.__edad}\n{cuentas_str}"

    def agregarCuenta(self, cuenta):
        if isinstance(cuenta, Cuenta):  
            self.cuentas.append(cuenta)
        else:
            print("Error: El objeto no es una instancia de la clase Cuenta.")
    
    def eliminarCuenta(self, indice):
        if 0 <= indice < len(self.cuentas):
            self.cuentas.pop(indice)  
        else:
            print("Error: Índice inválido.")
    
    def infoCuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)  




@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

class Cuenta:
    def __init__(self, valor, tipo):
        
        self.__saldo = valor
        self.__tipo = tipo
        
    def imprimirDetalles(self):
        print("saldo::", self.__saldo)
        print("tipo::", self.__tipo)
        
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
    
    def __str__(self):
        return "Tipo: " + str(self.__tipo) + "\nSaldo: " + str(self.__saldo)



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