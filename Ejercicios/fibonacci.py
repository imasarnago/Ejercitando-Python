

""" The Fibonacci numbers are the numbers in the following integer sequence.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .... """



fibo_dic = dict()

def fibo (n:int) -> int:
    """Calculará el número de fibonacci en la posición indicada (n-ésimo)

    Args:
        n (int): Toma un número entero con el cual se calculará fibonacci 
    
    Returns:
        int: Fibonacci en el índice ingresado ingresado
    """
    
    if n == 1 or n == 0:
        return 1
    elif n<0:
        raise Exception ("Error. Ha ingresado un número negativo")
    elif n>1:
        if n in fibo_dic:
            return fibo_dic[n]
        else:
            res = fibo (n-1)+fibo(n-2)
            fibo_dic[n] = res
            return res
    else:
        raise Exception ("Algo salió muy mal")
    
#print (fibo (7))