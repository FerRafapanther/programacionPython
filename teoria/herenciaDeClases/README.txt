
# Fecha: junio, 2025
# @version: 1.5
# @autor: FernandoRafaelLopezSolano


README CLIENTE
En este archivo se encuentra la Clase Cliente con los siguientes atributos:
nombre
direccion
edad
cuentas

y se definiero los siguientes metodos_
def __init__
def imprimirDetalles
def agregarCuenta
def eliminarCuenta
def infoCuentas
def _str__

----------------------------------------------------------------------------------------------------------------------

README MENU
En este archivo se encuentra la Clase Menu, con la observacion siguiente:
debido al diseño del Menu establecido, se tuvo que modificar esta Clase, por lo cual
esta Clase ya no cuenta con metodos y atributos, de los cuales fueron colocados en la
Clase MenuPrincipal y la Clase MenuSecundario

----------------------------------------------------------------------------------------------------------------------

README CUENTA
En este archivo se encuentra la Clase Cuenta con los siguientes atributos:
saldo
propietario

La Clase Cuenta tiene los siguientes metodos
def __init__
def imprimirDetalles
def retirar
def depositar
def __str__ 
con la observacion de que los metodos def retirar y def depositar son los metodos que realizan la operacion que implica realizar un retiro
y un deposito.
----------------------------------------------------------------------------------------------------------------------------------------------

README MENUPRINCIPAL
En este archivo se encuentra la Clase MenuPrincipal

La Clase tiene definido el siguiente atributo:
mensaje

La Clase MenuPrincipal es una de las Clases que fueron creadas recientemente, por el diseño que se planteo para el Menu del banco,
por lo cual algunos metodos de la Clase Menu (recordemos que la Clase Menu esta vacia) ahora estan definidos en esta Clase MenuPrincipal

Su objetivo de esta nueva Clase es separar la logica del Menu del banco, que la separaremos mediante 2 menus, en este caso la Clase MenuPrincipal es la que permite al usuario seleccionar la cuenta con la que desea trabajar en el banco.

por lo cual los metodos de la Clase MenuPrincipal son:
def __init__
def darBienvenida   #Este metodo se encarga de dar la bienvenida al usuario que ingresa al banco
def menuCuentas     #Este metodo permite al usuario escoger la cuenta en la que desea trabajar en el banco, lo hace presentando una serie de opciones.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

README MENUSECUNDARIO
En este archivo se encuentra la Clase MenuSecundario
Su objetivo de esta nueva Clase es separar la logica del Menu del banco, que la separaremos mediante 2 menus, en este caso la Clase MenuSecundario es la Clase que permite al usuario que, cuando haya seleccionado una cuenta en la que desea trabajar ahora aparezca otro menu
solo que este menu permite seleccionar la operacion que desea realizar el usuario en la cuenta que selecciono, ya sea que desea realizar un retiro o un deposito, o tambien si desea volver al menu principal.
su atributo que tiene esta clase es el siguiente:
cuenta

los metodos que tiene esta Clase MenuSecundario son:
def __init__
def realizar operacion     #Este metodo es aquel que permite que permite al usuario seleccionar la operacion que desea realizar en la cuenta que selecciono en el MenuPrincipal
def opcionRetirar          #Este Metodo tiene la funcion de que si el usuario escogio en alguna cuenta realizar un retiro, entonces llama al metodo retirar definido en la clase Cuenta
def opcionDepositar         #Este Metodo tiene la funcion de que si el usuario escogio en alguna cuenta realizar un deposito, entonces llama al metodo depositar definido en la clase Cuenta

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

README CUENTACREDITO
En este archivo se encuentra la Clase CuentaCredito, que es una Cuenta Hija de la Clase Cuenta
La clase CuentaCredito al ser una clase Hija de la Clase Cuenta, heredo 2 atributos de la clase Cuenta, que son los siguientes:

saldo
propietario

La clase CuentaCredito tiene esos atributos y ademas otro, que este ya es propio de la clase CuentaCredito, que es el tipo.

la clase CuentaCredito tiene los siguientes metodos:
def __init__
def __str__

--------------------------------------------------------------------------------------------------------------------------------------------------

README CUENTADEBITO

En este archivo se encuentra la Clase CuentaDebito, que es una Cuenta Hija de la Clase Cuenta
La clase CuentaDebito al ser una clase Hija de la Clase Cuenta, heredo 2 atributos de la clase Cuenta, que son los siguientes:

saldo
propietario

La clase CuentaDebito tiene esos atributos y ademas otro, que este ya es propio de la clase CuentaDebito, que es el tipo.

la clase CuentaDebito tiene los siguientes metodos:
def __init__
def __str__

----------------------------------------------------------------------------------------------------------------------------------------------

README CUENTANOMINA

En este archivo se encuentra la Clase CuentaNomina, que es una Cuenta Hija de la Clase Cuenta
La clase CuentaNomina al ser una clase Hija de la Clase Cuenta, heredo 2 atributos de la clase Cuenta, que son los siguientes:

saldo
propietario

La clase CuentaNomina tiene esos atributos y ademas otro, que este ya es propio de la clase CuentaNomina, que es el tipo.

la clase CuentaNomina tiene los siguientes metodos:
def __init__
def __str__

----------------------------------------------------------------------------------------------------------------------------------------------

README PRUEBASCUENTAS
En este archivo se encuentra la clase PruebasCuentas, en esta clase se realiza la prueba de las clases anteriores que conforman al sistema del Banco.

Esta clase no tiene atributos, pero si tiene metodos, que fueron necesarios para iniciar la prueba del codigo ya en conjunto:
los metodos de esta clase son los siguientes:

def __init__
def iniciar #Este metodo permite mandar a llamar los metodos que dan la bienvenida al banco y al menu de cuentas

Ademas se agrego esta linea de codigo, que asegura que el bloque de codigo de la clase PruebasCuentas solo se ejecute desde esta clase.
if __name__ == "__main__":
    pruebas = PruebasCuentas()
    pruebas.iniciar()
