# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:20:41 2025

@author: Rocket
"""
# Fecha: Marzo, 2025
# @version: 1.3
# @autor: FernandoRafaelLopezSolano

from Menu import *
from Cliente import *
from Cuenta import *

class Main:
    pass

cuenta1 = Cuenta(450, "debito", "Fernando")
cliente1 = Cliente("Fernando", "Ciudad de México", 19, cuenta1)

print("Detalles del cliente:")
print(f"Nombre: {cliente1.get_nombre()}")
print(f"Dirección: {cliente1.get_direccion()}")
print(f"Edad: {cliente1.get_edad()}")
print("Detalles de la cuenta:")
cliente1.imprimirDetalles()

menu1 = Menu("Bienvenido a Banxico", cuenta1)
menu1.darBienvenida()
menu1.desplegarOpciones()

