"""
Definir una función max_de_tres() que tome tres números como argumentos y devuelva el mayor de ellos
"""

def max_de_tres(n1:int,n2:int,n3:int):
    """Tomo tres números y devuelvo el más grande

    Args:
        n1 (int): Primer argumento a comparar
        n2 (int): Segundo argumento a comparar
        n3 (int): Tercer argumento a comparar
        
    Returns:
        int: Mayor de los tres
    """
    
    if (n1>n2):
        if (n1>n3):
            return n1
        else:
            return n3
    elif(n2>n1):
        if (n2>n3):
            return n2
        else:
            return n3
    elif(n3>n1):
        if (n3>n2):
            return n3
        else:
            return n2
    elif (n1==n2 or n2==n3 or n3 ==n1):
        raise Exception ("Los números deben ser diferentes")
    else:
        raise Exception ("Ha ocurrido un error con los numeros ingresados")

      
      
      
                          # Otra forma de hacerlo es la siguiente:


from mayor import custom_max as maximo
    
def max_de_tres_2(n1,n2,n3):
    """Tomo tres números y devuelvo el más grande

    Args:
        n1 (int): Primer argumento a comparar
        n2 (int): Segundo argumento a comparar
        n3 (int): Tercer argumento a comparar
        
    Returns:
        int: Mayor de los tres
    """
    
    """ 
    Puedo usar que:
    si  a>b>c
    ==> puedo afirmar lo siguiente:
    a>c  y  b>c
    Entonces:
    """
    
    
    max_primeros_dos = maximo (n1,n2)
    resultado = maximo (max_primeros_dos,n3)
    return (resultado)

