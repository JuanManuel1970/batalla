import pygame
import random
import sys


def pedir_nombre(puntaje, pantalla)->str:
    """
    Funcion : Solicita al usuario que ingrese su nombre a través de un campo de texto en la pantalla.

    Parámetros:El puntaje actual del jugador que se muestra en la pantalla y La pantalla de Pygame donde se dibujarán los resultados                      

    Retorna:El nombre ingresado por el jugador.

    """
    fuente = pygame.font.SysFont('Arial', 23, bold = True)
    input_box = pygame.Rect(250, 300, 200, 40)
    color = pygame.Color(141, 182, 205)
    text = ''
    pantalla.fill((255, 255, 255))  
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
    pantalla.blit(texto_puntaje, (250, 250))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  
                    return text
                elif evento.key == pygame.K_BACKSPACE:  
                    text = text[0:-1]
                else:  
                    text += evento.unicode 

        pantalla.fill((255, 255, 255)) 
        pantalla.blit(texto_puntaje, (250, 250)) 

        
        pygame.draw.rect(pantalla, color, input_box, 2)
        texto_nombre = fuente.render(text, True, (0, 0, 0))
        pantalla.blit(texto_nombre, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()  
        

def poner_naves(matriz, naves)->list:
    """
    Funcion :Coloca las naves en un tablero representado por una matriz

    Parámetros: Recibe la matriz  que representa el tablero de juego y las naves que es una lista de tuplas con los datos (nombre , tamnanio y cantidad)
          
    Retorna:Una lista de listas con las coordenadas de las naves colocadas en el tablero

    """
    tamano_matriz = len(matriz)  
    coordenadas_naves = []  
    for naves,largo, cantidad in naves:
        for _ in range(cantidad): 
            colocada = False  
            while not colocada:
                orientacion = random.choice(["horizontal", "vertical"])  
                fila = random.randint(0, tamano_matriz - 1)
                columna = random.randint(0, tamano_matriz - 1)
                if orientacion == "horizontal" and columna + largo <= tamano_matriz:
                    espacio_libre = True  
                    for i in range(largo):
                        if matriz[fila][columna + i] != 0: 
                            espacio_libre = False
                            break  

                    if espacio_libre:  
                        for i in range(largo):
                            matriz[fila][columna + i] = 1        
                        coordenadas_naves.append([(fila, columna + i) for i in range(largo)])
                        colocada = True  
                elif orientacion == "vertical" and fila + largo <= tamano_matriz:
                    espacio_libre = True  
                    for i in range(largo):
                        if matriz[fila + i][columna] != 0: 
                            espacio_libre = False
                            break  

                    if espacio_libre: 
                        for i in range(largo):
                            matriz[fila + i][columna] = 1 
                       
                        coordenadas_naves.append([(fila + i, columna) for i in range(largo)])
                        colocada = True 
    return coordenadas_naves  

