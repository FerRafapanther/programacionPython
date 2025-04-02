# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:20:41 2025

@author: Rocket
"""
# Fecha: abril, 2025
# @version: 1.4
# @autor: FernandoRafaelLopezSolano

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
