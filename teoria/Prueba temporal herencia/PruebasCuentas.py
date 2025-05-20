# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:50:38 2025

@author: Rocket
"""
    
from CuentaDebito import *
from CuentaCredito import *
from CuentaNomina import *
from Menu import *
   
# Crear cuentas hijas
cuenta_debito = CuentaDebito(450, "Fernando")
cuenta_credito = CuentaCredito(200, "Fernando")
cuenta_nomina = CuentaNomina(340, "Fernando")

# Crear lista con las cuentas
cuentas_usuario = [cuenta_debito, cuenta_credito, cuenta_nomina]

# Iniciar menú con mensaje de bienvenida
menu = Menu("Bienvenido al sistema bancario.", cuentas_usuario)

# Ejecutar flujo del menú interactivo
menu.darBienvenida()
menu.menuCuentas()