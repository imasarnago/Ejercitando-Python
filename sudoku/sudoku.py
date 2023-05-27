board = board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]


class ValidateSudoku:
    def __init__(self,tablero) -> None:
        self.tablero = tablero
        self.columna_hecha_lista = []

    def chequeo_general(self):
        
        # Chequear que el tablero introducido sea un tablero 9x9 
         
        assert len(self.tablero) == 9, "El tablero ingresado no respeta el formato 9x9" 
        for fila in self.tablero:
            assert len(fila) == 9, "El tablero ingresado no respeta el formato 9x9"
            
    def chequeo_filas (self, lista_a_chequear='tablero_general'):
        if lista_a_chequear == 'tablero_general':
            lista_a_chequear = self.tablero
    
        for lista in lista_a_chequear:
            for elemento in lista:
                if elemento != '.':
                    assert lista.count(elemento) == 1, "El tablero ingresado no respeta el formato 9x9"
                    

    def chequeo_columnas(self):
        for indice_columna in range (0,9):
            for indice_fila in range (0,9):
                self.columna_hecha_lista.append (self.tablero[indice_columna][indice_fila])
            self.chequeo_filas(self.columna_hecha_lista)
            self.columna_hecha_lista.clear()        
        


    def chequeo_subcuadritos (self):
        self.chequeo_3_subcuadritos(0,3)
        self.chequeo_3_subcuadritos(3,6)
        self.chequeo_3_subcuadritos(6,9)
    
    def chequeo_3_subcuadritos(self,param1,param2):
        self.columna_hecha_lista.clear()
        for indice_columna in range (0,9):
            if indice_columna == 3 or indice_columna==6:
                self.columna_hecha_lista.clear()
            for indice_fila in range(param1,param2):
                self.columna_hecha_lista.append(self.tablero[indice_fila][indice_columna])
                if (len(self.columna_hecha_lista)) == 9:
                    self.chequeo_filas(self.columna_hecha_lista)      




   
if __name__ == "__main__":
    sudoku = ValidateSudoku(board)
    sudoku.chequeo_general()
    sudoku.chequeo_filas()
    sudoku.chequeo_columnas()
    sudoku.chequeo_subcuadritos()

    print ("El tablero de Sudoku ingresado es válido")