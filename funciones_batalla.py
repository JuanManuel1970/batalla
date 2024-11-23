import pygame
import random
import sys
from configuracion_batalla import *
pygame.init()
fuente = pygame.font.SysFont('Arial', 25)
mensajes = []



def pedir_nombre(puntaje:int, pantalla:pygame.surface)->str:

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
        

def poner_naves(matriz:list, naves:list)->list:
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


def dibujar_tablero(matriz:list, intentos:list, tamano_matriz:int)->None:
    """
    Funcion : Dibuja un tablero de juego en la pantalla de Pygame

    Parámetros: Una matriz  que representa el tablero de juego . 
    Intentos :una segunda matriz de igual tamaño que la primera donde cada celda
    contiene 1 o 0 
    tamano_matriz : El tamaño del tablero de juego
        
    Retorno : None. 

    """
   
    tamano_celda = min(ANCHO, ALTO) // tamano_matriz  

    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            x = columna * tamano_celda
            y = fila * tamano_celda      
            pygame.draw.rect(pantalla, BLANCO, (x, y, tamano_celda, tamano_celda))  # ---se dibuja el fondo blanco de la celda---  
            pygame.draw.rect(pantalla, NEGRO, (x, y, tamano_celda, tamano_celda), 2)     # ---se dibuja el borde negro de la celda---
        
            if intentos[fila][columna] == 1:     # ---si el disparo da en esta celda , le pego a la nave (pone un uno)---
                # --- dibuja una X roja que cruza la celda---
                pygame.draw.line(pantalla, (255, 0, 0), (x, y), (x + tamano_celda, y + tamano_celda), 3)  
                pygame.draw.line(pantalla, (255, 0, 0), (x + tamano_celda, y), (x, y + tamano_celda), 3)  
          
            elif intentos[fila][columna] == -1:   # ---si el disparo da en esta celda es un fallo (pone un cero)---
                centro = (x + tamano_celda // 2, y + tamano_celda // 2)
                pygame.draw.circle(pantalla, (0, 0, 255), centro, tamano_celda // 3, 2)  # ---dibuja un círculo  en de la celda---





def pantalla_puntajes()->None:
    """
    Funcion : Muestra una pantalla con los 5 puntajes más altos del juego

    Parámetros: No recibe parámetros

    Retorna: No retorna ningún valor
    """

    corriendo = True
    fondo = pygame.transform.scale(pygame.image.load('imagenes/fondo2.jpg'), (ANCHO, ALTO))

    while corriendo:
        pantalla.blit(fondo, (0, 0))
        mostrar_texto("Puntajes", NEGRO, 300, 30)
        with open("puntajes.txt", "a+") as archivo:
            archivo.seek(0) 
            puntajes = [linea.strip().split(",") for linea in archivo.readlines() if linea.strip()]      
            puntajes.sort(key=lambda x: x[1], reverse=True)
        for i in range(min(3, len(puntajes))):
            nombre, puntos = puntajes[i]
            mostrar_texto(f"{i+1}. {nombre}: {puntos} puntos", NEGRO, 300, 150 + i * 30)

       
        for i in range(len(puntajes), 3):
            mostrar_texto(f"{i+1}. No hay puntajes", NEGRO, 300, 150 + i * 30)
       
        dibujar_boton("Volver", 300, 360, 200, 50, (200, 200, 0), NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 500 and 360 <= y <= 410:
                    corriendo = False

        pygame.display.flip()





def crear_matriz(tamano_matriz:int)->list:

    """
    Función: Crea una matriz cuadrada 

    Parámetros: El tamaño de la matriz 

    Retorna: Una matriz 

    """
    matriz = [] 
    for _ in range(tamano_matriz):
        fila = [0] * tamano_matriz 
        matriz.append(fila) 
    return matriz











######################### FUNCIONES AUXILIARES ################################
def mostrar_texto(texto, color, x, y):
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))

def dibujar_boton(texto, x, y, ancho, alto, color_boton, color_texto):
    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto),border_radius=85)
    mostrar_texto(texto, color_texto, x + 20, y + 20) 


def mostrar_puntaje(puntaje):
    fuente = pygame.font.SysFont("Arial", 25)  
    texto = fuente.render(f"Puntaje: {puntaje:04d}", True, NEGRO) 
    pantalla.blit(texto, (600, 10)) 

def guardar_puntaje(nombre, puntaje):
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")

def agregar_mensaje(mensaje):
    if len(mensajes) >= 5:
        mensajes.pop(0)  # Elimina el mensaje más antiguo si ya hay 3
    mensajes.append(mensaje)  # Agrega el nuevo mensaje

def mostrar_mensajes():
    y_pos = 150  
    x_pos = 610  
    fuente_mensajes = pygame.font.SysFont('Arial', 18)  
    for mensaje in mensajes:
        texto_renderizado = fuente_mensajes.render(mensaje, True, 'blue')  
        pantalla.blit(texto_renderizado, (x_pos, y_pos)) 
        y_pos += 20


def mostrar_texto(texto, color, x, y):
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))




def crear_boton(texto, color, x, y, ancho, alto):
    pygame.draw.rect(pantalla, color, (x, y, ancho, alto))
    mostrar_texto(texto, BLANCO, x + 10, y + 10)



def boton_presionado(x, y, ancho, alto, mouse_x, mouse_y):
    return x < mouse_x < x + ancho and y < mouse_y < y + alto



def dibujar_boton_musica(x, y, ancho, alto, color_boton, color_texto, music_on):
    texto = "Música: ON" if music_on else "Música: OFF"
    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto))
    mostrar_texto(texto, color_texto, x + 20, y + 20)




