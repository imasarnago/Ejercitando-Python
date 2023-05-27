

# Usaré lo siguiente para luego cambiarle los colores a las letras : 
colors = {
    'green' : '\033[92m',
    'yellow' : '\033[93m',
    'red' : '033[91m',
    'ENDC' : '\033[0m',
}
def color_letra (letra,color):
    return colors[color] + letra + colors["ENDC"]


# Iniciar Juego

word = 'trineo'
board = []
win = False

print (f"Iniciando juego!. A continuación ingrese su palabra de seis caracteres : ")

for i in range (6):
    board.append(['_' for l in range (6)])

game_contador = 0

while (not win) and (game_contador < len (word)):
    text = ""
    while len(text) != len(word):
        print (f"La palabra DEBE TENER {len(word)} cantidad de letras")
        text = input("ingrese la palabra: ")
        
        
    # Escribamos la lógica de victoria del juego
    
    if word == text:
        board[game_contador] = [l for l in text]        
        win = True
    
    # Escribamos la lógica de cuando la letra pertenece a la palabra pero no está donde queremos
    else:
        linea_de_texto = []
        for j in range (len(text)):
            if (text[j] == word[j]) :
                linea_de_texto.append(text[j])
            elif text[j] in word :
                linea_de_texto.append (color_letra(text[j],'yellow'))
            else:
                linea_de_texto.append (color_letra(text[j],'ENDC'))
        board[game_contador] = linea_de_texto 
        
        
    # Dibujando el tablero de juego en la consola
    for i in range (6):
        print (" ".join(board[i]))
        print("\n")

    game_contador += 1
    
if win: 
    print ("¡  YEEAAAHHHH  !")
else:
    print (" Oh rayos, inténtalo nuevamente :( ")