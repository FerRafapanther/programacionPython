# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:44:46 2025

@author: Equipo 34
"""
from Cliente import Cliente
from Cuenta import Cuenta
from Menu import Menu


class Main:
    pass



cliente1= Cliente("Fernando", "ciudad de mexico", 19)
print(cliente1.nombre)
print(cliente1.direccion)
print(cliente1.edad)

cliente1.imprimirDetalles()

cuenta1= Cuenta(450, "debito", "Fernando")
print(cuenta1.saldo)
print(cuenta1.tipo)
print(cuenta1.propietario)
cuenta1.retirar(100)
print("Saldo después del retiro: ", cuenta1.saldo)
cuenta1.depositar(200)
print("Saldo después del depósito: ", cuenta1.saldo)
print(cuenta1.saldo)

cuenta1.imprimirDetalles()


cuenta1 = Cuenta(450, "debito", "Fernando")
cliente1 = Cliente("Fernando", "Ciudad de México", 19, cuenta1)

print("Detalles del cliente:")
print(f"Nombre: {cliente1._Cliente__nombre}")
print(f"Dirección: {cliente1._Cliente__direccion}")
print(f"Edad: {cliente1._Cliente__edad}")
print("Detalles de la cuenta:")
cliente1.imprimirDetalles()




