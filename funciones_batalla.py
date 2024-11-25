import pygame
import random
import sys
from configuracion_batalla import *



pygame.init()
fuente = pygame.font.SysFont('Arial', 25)
mensajes = []
puntaje = 0 


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

        # Obtener la posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verificar si el mouse está sobre el botón "Volver"
        hover_volver = 300 <= mouse_x <= 500 and 360 <= mouse_y <= 410
       
        dibujar_boton("Volver", 300, 360, 200, 50, color_base, color_texto, hover=hover_volver)

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

def mostrar_texto(texto: str, color: tuple, x: int, y: int, centrado: bool = False) -> None:
    """
    Función: Muestra un texto en la pantalla.
    Parámetros:
    texto : El texto a mostrar.
    color: Color del texto en formato RGB.
    x : Posición horizontal del texto.
    y : Posición vertical del texto.
    Retorno: None
    """
    fuente = pygame.font.Font(None, 36)  # Fuente y tamaño
    texto_renderizado = fuente.render(texto, True, color)
    texto_rect = texto_renderizado.get_rect(center=(x, y) if centrado else (0, 0))
    pantalla.blit(texto_renderizado, texto_rect if centrado else (x, y))



def mostrar_puntaje(puntaje: int) -> None:
    """
    Función: Muestra el puntaje en la pantalla.
    Parámetros:El puntaje a mostrar en pantalla.
    Retorno:None
    """
    fuente = pygame.font.SysFont("Arial", 25)  
    texto = fuente.render(f"Puntaje: {puntaje:04d}", True, NEGRO) 
    pantalla.blit(texto, (600, 10)) 



def guardar_puntaje(nombre: str, puntaje: int) -> None:
    """
    Función: Guarda el puntaje en un archivo de texto.
    Parámetros:El nombre del jugador y el puntaje obtenido por el jugador.
    Retorno: None
    """
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")



def agregar_mensaje(mensaje: str) -> None:
    """
    Función: Agrega un mensaje a la lista de mensajes, eliminando el más antiguo si hay más de 5 mensajes.
    Parámetros:El mensaje a agregar a la lista de mensajes.
    Retorno:None
    """
    if len(mensajes) >= 5:
        mensajes.pop(0)  # Elimina el mensaje más antiguo si ya hay 3
    mensajes.append(mensaje)  # Agrega el nuevo mensaje


def mostrar_mensajes() -> None:
    """
    Función: Muestra los mensajes almacenados en la lista de mensajes en la pantalla
    Parámetros: Ninguno
    Retorno: None
    """
    y_pos = 150  
    x_pos = 610  
    fuente_mensajes = pygame.font.SysFont('Arial', 18)  
    for mensaje in mensajes:
        texto_renderizado = fuente_mensajes.render(mensaje, True, 'blue')  
        pantalla.blit(texto_renderizado, (x_pos, y_pos)) 
        y_pos += 20



def boton_presionado(x: int, y: int, ancho: int, alto: int, mouse_x: int, mouse_y: int) -> bool:
    """
    Función: Verifica si un clic de ratón ha ocurrido dentro de las coordenadas de un botón
    Parámetros:
    x : La coordenada x de la esquina superior izquierda del botón.
    y : La coordenada y de la esquina superior izquierda del botón.
    ancho : El ancho del botón.
    alto : El alto del botón.
    mouse_x : La coordenada x del clic del ratón.
    mouse_y : La coordenada y del clic del ratón.
    Retorno:bool: Devuelve True si el clic del ratón está dentro de los límites del botón, de lo contrario False.
    """
    return x < mouse_x < x + ancho and y < mouse_y < y + alto



def dibujar_boton(texto, x, y, ancho, alto, color_base, color_texto, hover=False, color_borde=(0, 0, 0), radio_bordes=15):
    """
    Dibuja un botón redondeado con borde y texto, y opcionalmente cambia de color si el mouse está sobre él.
    
    Parámetros:
    texto (str): Texto a mostrar en el botón.
    x, y (int): Coordenadas de la esquina superior izquierda del botón.
    ancho, alto (int): Dimensiones del botón.
    color_base (tuple): Color principal del botón.
    color_texto (tuple): Color del texto.
    hover (bool): Indica si el botón está en estado "hover" (cursor encima).
    color_borde (tuple): Color del borde del botón.
    radio_bordes (int): Radio de los bordes redondeados.
    """
    # Cambiar color si el botón está en estado hover
    if hover:
        # Crear un color base más saturado o brillante
        color_satinado = (min(color_base[0] + 40, 255),  # Aumenta el componente R
                          min(color_base[1] + 40, 255),  # Aumenta el componente G
                          min(color_base[2] + 40, 255))  # Aumenta el componente B
        color_base = color_satinado

    # Dibujar el borde redondeado del botón
    pygame.draw.rect(pantalla, color_borde, (x - 1, y - 1, ancho + 10, alto + 10), border_radius=radio_bordes)

    # Dibujar el rectángulo del botón con bordes redondeados
    pygame.draw.rect(pantalla, color_base, (x, y, ancho, alto), border_radius=radio_bordes)

    # Agregar texto centrado
    fuente = pygame.font.Font(None, 36)  # Tamaño de fuente ajustable
    texto_superficie = fuente.render(texto, True, color_texto)
    texto_rect = texto_superficie.get_rect(center=(x + ancho // 2, y + alto // 2))
    pantalla.blit(texto_superficie, texto_rect)
