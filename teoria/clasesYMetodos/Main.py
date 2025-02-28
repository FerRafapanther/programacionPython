# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:20:41 2025

@author: Rocket
"""
# Fecha: Febrero, 2025
# @version: 1.1
# @autor: FernandoRafaelLopezSolano

from Menu import *
from Cliente import *
from Cuenta import *

class Main:
    pass

menu1= Menu("Bienvenido a banxico")
menu1.darBienvenida()

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

