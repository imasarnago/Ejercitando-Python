"""

Escribir un programa que permita controlar con validación el ingreso a un sitio web. 
Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"),
el programa debe permitir al usuario ingresar sus credenciales. 
Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. 
Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: 
"Acceso concedido" o "Se ha bloqueado la cuenta"


"""
USUARIO = "admin"
CONTRASEÑA = 123456

usuario = input ("Ingrese su usuario : ")
contraseña = int (input("Ingrese su contraseña : "))
CANTIDAD_INTENTOS = 3

if (usuario != USUARIO) or (contraseña != CONTRASEÑA):
    print (f"Le quedan {CANTIDAD_INTENTOS} intentos")
    for x in range (CANTIDAD_INTENTOS):
        usuario = input ("Ingrese su usuario : ")
        contraseña = int (input("Ingrese su contraseña : "))
        CANTIDAD_INTENTOS += -1
        print (f"Le quedan {CANTIDAD_INTENTOS} intentos")
        if CANTIDAD_INTENTOS == 0:
            print ("Se ha bloqueado la cuenta :( ")
else:
    print ("¡Acceso concedido!")
    
