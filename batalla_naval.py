# Desarrollar en Python:
# Videojuego Batalla Naval, que tendrá los siguientes datos:
# ● Matriz de 10 filas por 10 columnas. 
# ● Datos para llenar la matriz de 10 filas por 10 columnas. 
# ● Datos para colocar en la matriz de 10 filas por 10 columnas cada una de las naves. 
# ● Dificultad:  
# Nivel Fácil: matriz de 10 filas por 10 columnas. 
# Nivel Medio: matriz de 20 filas por 20 columnas y duplicar la cantidad de naves. o 
# Nivel Difícil: matriz de 40 filas por 40 columnas y triplicar la cantidad de naves. 
# 1 Requerimientos: 
# A. Para el estado inicial: desarrollar una función que realice la creación dinámica de una matriz de 10 filas por 10 columnas. 
# En la misma se deberá incluir ceros para el agua y unos consecutivos para las naves. Las naves pueden ser horizontales y/o verticales. 
# Las naves deben ser generadas de la siguiente manera: 
#  Cuatro (4) submarinos de un (1) casillero  Tres (3) destructores de dos (2) casilleros  Dos (2) cruceros de tres (3) casilleros  Un (1) acorazado de cuatro (4) casilleros 
# B. Crear una pantalla de inicio, con cuatro (4) botones:   Nivel  Jugar  Ver Puntajes  Salir La pantalla deberá tener:   Una imagen cubriendo completamente el fondo. 
#  Sonido de fondo.  Al hacer clic en el botón Jugar se iniciará el juego. C. En la pantalla del juego:   Habrá un tablero donde a cada casillero del mismo 
# le corresponderá un elemento de la matriz.  Crear un (1) botón con la etiqueta Reiniciar. D. Al comenzar el juego se deberá imprimir el Puntaje en 0000 donde se irá 
# decrementando en un (1) punto por cada disparo errado (pudiendo tener puntaje negativo). Cada disparo acertado sumará cinco (5) puntos, al hundir la nave se obtendrán diez 
# (10) puntos extras por cada elemento que compone la misma.  Por ejemplo: Si la nave es de tres (3) elementos consecutivos de la matriz, sumará 30 puntos, además de los cinco
# (5) puntos sumados anteriormente por haber averiado cada uno de los elementos que la componen. E. Al hacer clic en uno de los casilleros del tablero se efectuará el disparo. 
# No se podrá efectuar el disparo sobre el mismo casillero más de una vez. F. Al disparar:  Si el disparo es acertado (da en el blanco): o Si la nave es averiada, se debe sumar
# cinco (5) puntos. o Si la nave es hundida, se debe sumar diez (10) puntos por cada elemento que contenga la misma.  Si el disparo hace agua (no da en el blanco), se debe restar
# un (1) punto. G. Al hacer clic en el botón Reiniciar se reiniciará el juego, y el puntaje volverá a estar en 0000. 2 H. Antes de comenzar o una vez terminado el juego se deberá 
# pedir el nombre al usuario (Nick), guardar ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio. I. Al ingresar a la pantalla inicial y hacer clic en el botón
# Ver Puntajes, se deberá mostrar los 3 (tres) mejores puntajes ordenados de mayor a menor, junto con su nombre de usuario (Nick) correspondiente. Debe haber un (1) botón para 
# volver al menú principal. OPCIONALES:  Nivel de dificultad. ● Pantalla de inicio: agregar un (1) botón para activar / desactivar el sonido de fondo.  Al disparar: o Reproducir
# un sonido de disparo acertado. o Reproducir un sonido de disparo errado.  Agregar imágenes, sonidos, y animaciones donde corresponda. 
from funciones_batalla import *
from configuracion_batalla import *
import pygame
import random
import sys
import os



pygame.init()



fuente = pygame.font.SysFont('Arial', 36)

music_on = True
puntaje = 0 


def mostrar_texto(texto, color, x, y):
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))


def dibujar_boton(texto, x, y, ancho, alto, color_boton, color_texto):
    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto))
    mostrar_texto(texto, color_texto, x + 20, y + 20) 


def mostrar_puntaje(puntaje):
    fuente = pygame.font.SysFont("Arial", 36)  
    texto = fuente.render(f"Puntaje: {puntaje:04d}", True, NEGRO) 
    pantalla.blit(texto, (600, 10))  


def guardar_puntaje(nombre, puntaje):
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")

        

def pedir_nombre(puntaje):
    fuente = pygame.font.SysFont("Arial", 30) 
    input_box = pygame.Rect(250, 300, 200, 40)  
    color = pygame.Color(141, 182, 205)  
    text = ''  
    clock = pygame.time.Clock()  
    pantalla.fill((255, 255, 255))  
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
    pantalla.blit(texto_puntaje, (250, 250))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:  
                if input_box.collidepoint(evento.pos):  
                    color = pygame.Color(28, 134, 238)  
                else:
                    color = pygame.Color(141, 182, 205) 
            elif evento.type == pygame.KEYDOWN:  
                if evento.key == pygame.K_RETURN:  
                    return text  
                elif evento.key == pygame.K_BACKSPACE: 
                    text = text[:-1]
                else: 
                    text += evento.unicode
  
        pygame.draw.rect(pantalla, color, input_box, 2)
        texto_nombre = fuente.render(text, True, (0, 0, 0))
        pantalla.blit(texto_nombre, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip() 
        clock.tick(30)  



def mostrar_texto(texto, color, x, y):
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))



def crear_boton(texto, color, x, y, ancho, alto):
    pygame.draw.rect(pantalla, color, (x, y, ancho, alto))
    mostrar_texto(texto, BLANCO, x + 10, y + 10)



def boton_presionado(x, y, ancho, alto, mouse_x, mouse_y):
    return x < mouse_x < x + ancho and y < mouse_y < y + alto



def reiniciar_juego(tamano_matriz, nivel):
    iniciar_juego(tamano_matriz, nivel)





def pantalla_inicio():
    nivel_predeterminado = "fácil"  
    music_on = True  

    while True:
        pantalla.blit(fondo, (0, 0))  
        mostrar_texto("Batalla Naval", NEGRO, 300, 50) 

        dibujar_boton("Nivel", 300, 140, 200, 60, (150, 0, 200), BLANCO)
        dibujar_boton("Jugar", 300, 220, 200, 50, (0, 0, 200), BLANCO)
        dibujar_boton("Ver Puntajes", 300, 290, 200, 50, (200, 200, 0), BLANCO)
        dibujar_boton("Salir", 300, 360, 200, 50, (200, 0, 0), BLANCO)
        dibujar_boton_musica(30, 30, 200, 50, (0, 200, 0), BLANCO, music_on)

        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 500 and 140 <= y <= 200: 
                    print("Seleccionar Nivel")
                    pantalla_seleccion_nivel() 
                elif 300 <= x <= 500 and 220 <= y <= 270:  
                    print("Iniciar Juego")
                    iniciar_juego(10, nivel=nivel_predeterminado)  
                elif 300 <= x <= 500 and 290 <= y <= 340:  
                    print("Ver Puntajes")
                    pantalla_puntajes()  
                elif 300 <= x <= 500 and 360 <= y <= 410:  
                    pygame.quit()
                    sys.exit()
                elif 30 <= x <= 230 and 30 <= y <= 80:  
                    music_on = not music_on 

                
                if music_on:
                    pygame.mixer.music.play(-1, 0.0) 
                else:
                    pygame.mixer.music.stop() 

        pygame.display.flip()  



def dibujar_boton_musica(x, y, ancho, alto, color_boton, color_texto, music_on):
    texto = "Música: ON" if music_on else "Música: OFF"
    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto))
    mostrar_texto(texto, color_texto, x + 20, y + 20)




def pantalla_seleccion_nivel():
    corriendo = True
    
  
    fondo = pygame.image.load('imagenes/fondo1.jpg')  
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))  
    
    while corriendo:
        pantalla.blit(fondo, (0, 0))  
        mostrar_texto("Selecciona el Nivel", NEGRO, 270, 50)  
        
      
        dibujar_boton("Fácil", 300, 150, 200, 50, (0, 200, 0), BLANCO)
        dibujar_boton("Medio", 300, 220, 200, 50, (0, 0, 200), BLANCO)
        dibujar_boton("Difícil", 300, 290, 200, 50, (200, 0, 0), BLANCO)
        
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN: 
                x, y = pygame.mouse.get_pos()
                
                if 300 <= x <= 500 and 150 <= y <= 200:  
                    print("Nivel Fácil seleccionado")
                    iniciar_juego(10, nivel="fácil")  
                    corriendo = False
                elif 300 <= x <= 500 and 220 <= y <= 270:  
                    print("Nivel Medio seleccionado")
                    iniciar_juego(20, nivel="medio")  
                    corriendo = False
                elif 300 <= x <= 500 and 290 <= y <= 340:
                    print("Nivel Difícil seleccionado")
                    iniciar_juego(40, nivel="difícil")  
                    corriendo = False    
        pygame.display.flip()  
 


def pantalla_puntajes():
    corriendo = True
    fondo = pygame.transform.scale(pygame.image.load('imagenes/fondo2.jpg'), (ANCHO, ALTO))

    while corriendo:
        pantalla.blit(fondo, (0, 0))
        mostrar_texto("Puntajes", NEGRO, 300, 50)

      
        with open("puntajes.txt", "a+") as archivo:
            archivo.seek(0) 
            puntajes = [linea.strip().split(",") for linea in archivo.readlines() if linea.strip()]

       
        puntajes = [(nombre, int(puntaje)) for nombre, puntaje in puntajes if len(puntaje) > 0]
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












def crear_matriz(tamano_matriz):
    matriz = [] 
    for _ in range(tamano_matriz):
        fila = [0] * tamano_matriz 
        matriz.append(fila) 
    return matriz




def iniciar_juego(tamano_matriz, nivel="fácil"):
   
    print(f"Iniciando juego con tablero de tamaño {tamano_matriz}x{tamano_matriz} y nivel {nivel}")
    matriz = crear_matriz(tamano_matriz)
    intentos = crear_matriz(tamano_matriz) 
    puntaje = 0
    aciertos = []
    

    if nivel == "medio":
        naves = [("acorazado", 4, 2), ("crucero", 3, 4), ("destructor", 2, 6), ("submarino", 1, 8)]
    elif nivel == "difícil":
        naves = [("acorazado", 4, 3), ("crucero", 3, 6), ("destructor", 2, 9), ("submarino", 1, 12)]
    else:
        naves = [("acorazado", 4, 1), ("crucero", 3, 2), ("destructor", 2, 3), ("submarino", 1, 4)]


    coordenadas_naves = poner_naves(matriz, naves)
    
    tamano_celda = min(ANCHO, ALTO) // tamano_matriz
    corriendo = True
    casillas_clicadas = 0
    total_casillas = tamano_matriz * tamano_matriz  

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

               
                fila, columna = y // tamano_celda, x // tamano_celda
                if 0 <= fila < tamano_matriz and 0 <= columna < tamano_matriz:
                    if intentos[fila][columna] == 0:  
                        casillas_clicadas += 1 
                        if matriz[fila][columna] == 1:  
                            intentos[fila][columna] = 1
                            puntaje += 5
                            aciertos.append((fila, columna)) 
                            sonido_acierto.play()
                            print(f"Acierto en ({fila}, {columna})")
                            
                            
                            for nave in coordenadas_naves:
                                if all(coordenada in aciertos for coordenada in nave):
                                    puntaje += len(nave) * 10 
                                    sonido_hundido.play() 

                                    print(f"Nave hundida! +{len(nave)*10} puntos")
                                    coordenadas_naves.remove(nave)  

                        else:  
                            intentos[fila][columna] = -1
                            puntaje -= 1
                            sonido_fallo.play() 

                            print(f"Fallo en ({fila}, {columna})")


               
                if 600 <= x <= 750 and 500 <= y <= 550:  
                    reiniciar_juego(tamano_matriz, nivel)
                elif 600 <= x <= 750 and 300 <= y <=400 :
                    pantalla_inicio()
                elif 600 <= x <= 750 and 440 <= y <= 490: 
                    pygame.quit()
                    sys.exit()

       
        if len(coordenadas_naves) == 0 or casillas_clicadas == total_casillas:
            print("Juego Terminado!")
            guardar_puntaje(pedir_nombre(puntaje), puntaje)  
            reiniciar_juego(tamano_matriz, nivel)  
  

        pantalla.fill(BLANCO)
        mostrar_puntaje(puntaje) 
        dibujar_tablero(matriz, intentos, tamano_matriz)
        dibujar_boton("Salir",      600, 440, 150, 50, (200, 0, 0), NEGRO)
        dibujar_boton("Reiniciar",  600, 500, 150, 50, (200, 200, 0), NEGRO)
        dibujar_boton("Inicio",     600, 300, 150, 50, (180, 200, 120), NEGRO)
        
        pygame.display.flip()




def poner_naves(matriz, naves):
    tamano_matriz = len(matriz)  
    coordenadas_naves = []  

   
    for nombre, largo, cantidad in naves:
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




def dibujar_tablero(matriz, intentos, tamano_matriz):
    tamano_celda = min(ANCHO, ALTO) // tamano_matriz  
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            x = columna * tamano_celda
            y = fila * tamano_celda
            pygame.draw.rect(pantalla, BLANCO, (x, y, tamano_celda, tamano_celda))
            pygame.draw.rect(pantalla, NEGRO, (x, y, tamano_celda, tamano_celda), 2)

         
            if intentos[fila][columna] == 1:  
                pygame.draw.line(pantalla, (255, 0, 0), (x, y), (x + tamano_celda, y + tamano_celda), 3)
                pygame.draw.line(pantalla, (255, 0, 0), (x + tamano_celda, y), (x, y + tamano_celda), 3)
            elif intentos[fila][columna] == -1: 
                centro = (x + tamano_celda // 2, y + tamano_celda // 2)
                pygame.draw.circle(pantalla, (0, 0, 255), centro, tamano_celda // 3, 2)




pantalla_inicio()