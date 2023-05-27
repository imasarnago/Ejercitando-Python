def invertir (cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = ""
    for n in range (longitud,1):
        n = abs(n)
        nueva_cadena += cadena[n]
    print (nueva_cadena)
invertir ("pepito")