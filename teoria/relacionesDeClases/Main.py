# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:20:41 2025

@author: Rocket
"""
# Fecha: Marzo, 2025
# @version: 1.2
# @autor: FernandoRafaelLopezSolano

from Menu import *
from Cliente import *
from Cuenta import *

class Main:
    pass

menu1= Menu("Bienvenido a banxico")
menu1.darBienvenida()
menu1.desplegarOpciones()

cuenta1= Cuenta(450, "debito", "Fernando")
cliente1= Cliente("Fernando", "ciudad de mexico", 19, cuenta1)
print("Detalles del cliente:")
print(f"Nombre: {cliente1.nombre}")
print(f"Dirección: {cliente1.direccion}")
print(f"Edad: {cliente1.edad}")
print("Detalles de la cuenta:")
cliente1.imprimirDetalles()


cuenta1.retirar(100)
print("Saldo después del retiro: ", cuenta1.saldo)
cuenta1.depositar(200)
print("Saldo después del depósito: ", cuenta1.saldo)
print(cuenta1.saldo)

cuenta1.imprimirDetalles()

