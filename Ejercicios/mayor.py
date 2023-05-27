def custom_max(n1:int,n2:int):
    """Dados dos numeros de entrada, regresa el máximo de ambos

    Args:
        n1 (int): Primer número a comparar
        n2 (int): Segundo número a comparar

    Returns:
        int: Mayor de ambos
    """
    if n2>n1:
        return n2
    elif n1>n2:
        return n1
    elif n1==n2:
        raise Exception ("¡Los valores no pueden ser iguales!")
    raise Exception ("Algo salió mal")