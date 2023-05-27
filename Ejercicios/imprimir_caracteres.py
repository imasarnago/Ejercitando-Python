def imprimir_n_caracteres(caracter,n):
    char = caracter
    for i in range (0,n-1):
        char += caracter
    print (char)
    
    
imprimir_n_caracteres('x',5)

def imprimir_n_caracteres_2(caracter,n):
    char = caracter*n
    print (char)
    
imprimir_n_caracteres_2('x',5)