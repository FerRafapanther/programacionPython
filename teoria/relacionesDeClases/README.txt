# Fecha: Marzo, 2025
# @version: 1.3
# @autor: FernandoRafaelLopezSolano

README MENU
En este archivo se encuentra la clase Menu con los 2 atributos:
mensajeBienvenida
cuenta
con la modificacion de que estos atributos ahora son privados.

y se definio los 5 metodos:
def __init__
def darBienvenida
def Opcionretirar
def OpcionDepositar
def OpcionSalir

con la observacion de que se agrego otro metodo, que es el siguiente:

def desplegarOpciones
dentro de este metodo, se agrego un bucle utilizando While, que permite escoger una de las 3 opciones disponibles



README CLIENTE
En este archivo se encuentra la clase Cliente con sus 4 atributos:
nombre
direccion
edad
cuenta
con la modificacion de que estos atributos ahora son privados

y se definio los 2 metodos:
def __init__
def __imprimir detalles

con la observacion de que se importo la clase Cuenta a la clase Cliente
tambien se agregaron estos metodos, para que los atributos privados se puedan ver en otras clases:
def get_nombre
def get_direccion
get_edad
get_cuenta


README CUENTA
En este archivo se encuentra la clase Cuenta con sus 3 atributos:
saldo
tipo
propietario
con la modificacion de que estos atributos ahora son privados

y se definio los 4 metodos:
def __init__
def __imprimir detalles
def retirar
def depositar

tambien se agregaron estos metodos, para que los atributos privados se puedan ver en otras clases:
get_saldo
set_saldo

con la observaciones que se agrego el uso del condicional "if" y "else" al momento de retirar o depositar cantidades.

REAME MAIN
En este archivo se encuentra la clase Main, aqui se realizan las pruebas de
los metodos de las clases:
Cliente
Cuenta
Menu
