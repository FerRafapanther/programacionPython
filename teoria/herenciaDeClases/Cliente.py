# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:25:39 2025

@author: Rocket
"""
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano

class Cliente:
    
    def __init__(self, nombre, direccion, edad, cuentas=None):
        
        self.__nombre=nombre
        self.__direccion=direccion
        self.__edad=edad
        self.__cuentas = cuentas if cuentas is not None else []
        
        
    def imprimirDetalles (self):
        
        print("nombre::", self.__nombre)
        print("direccion::", self.__direccion)
        print("edad::", self.__edad)
        print("Detalles de la cuentas:")
        if not self.__cuentas:
            print("Este cliente no tiene cuentas registradas.")
        else:
            for cuenta in self.__cuentas:
                cuenta.imprimirDetalles()
        
    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)
        print("Cuenta agregada exitosamente.")
        
    def eliminarCuenta(self, tipo_cuenta):
        original = len(self.__cuentas)
        self.__cuentas = [c for c in self.__cuentas if c._Cuenta__tipo != tipo_cuenta]
        if len(self.__cuentas) < original:
            print(f"Cuenta de tipo '{tipo_cuenta}' eliminada exitosamente.")
        else:
            print(f"No se encontró una cuenta de tipo '{tipo_cuenta}'.")
            
    def infoCuentas(self):

        if not self.__cuentas:
            print("Este cliente no tiene cuentas registradas.")
        else:
            print("Información de las cuentas del cliente:")
            for cuenta in self.__cuentas:
                print(cuenta)  # Esto llama a __str__()
    def __str__(self):
        detalle_cuentas_str = (
            "\n".join(str(cuenta) for cuenta in self.__cuentas)
            if self.__cuentas else "No hay cuentas registradas."
        )
        return (
            f"Nombre: {self.__nombre}\n"
            f"Dirección: {self.__direccion}\n"
            f"Edad: {self.__edad}\n"
            f"Detalles de las Cuentas:\n{detalle_cuentas_str}"
        )
