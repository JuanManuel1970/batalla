from funciones_batalla import *
from configuracion_batalla import *
import pygame
import sys


pygame.init()




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
                    pantalla_seleccion_nivel() 
                elif 300 <= x <= 500 and 220 <= y <= 270:  
                    iniciar_juego(10, nivel=nivel_predeterminado)  
                elif 300 <= x <= 500 and 290 <= y <= 340:  
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
                    iniciar_juego(10, nivel="fácil")  
                    corriendo = False
                elif 300 <= x <= 500 and 220 <= y <= 270:  
                    iniciar_juego(20, nivel="medio")  
                    corriendo = False
                elif 300 <= x <= 500 and 290 <= y <= 340:
                    iniciar_juego(40, nivel="difícil")  
                    corriendo = False    
        pygame.display.flip()  
 






def iniciar_juego(tamano_matriz, nivel="fácil"):
    # Crea la matriz 
    matriz = crear_matriz(tamano_matriz)
    intentos = crear_matriz(tamano_matriz)
    puntaje = 0
    aciertos = []
    
    # ---Segun el nivel coloca las naves---
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
                
                # ---Calcular la celda seleccionada en la matriz---
                fila, columna = y // tamano_celda, x // tamano_celda
                if 0 <= fila < tamano_matriz and 0 <= columna < tamano_matriz:
                    if intentos[fila][columna] == 0:  # ---Verifica si la celda se clickeo antes---
                        casillas_clicadas += 1  
                        if matriz[fila][columna] == 1:  
                            intentos[fila][columna] = 1
                            puntaje += 5
                            aciertos.append((fila, columna))  # ---Guarda si le pegamos a la neave---
                            sonido_acierto.play()
                            agregar_mensaje(f"Acierto en ({fila}, {columna})") 
                            print(f"Acierto en ({fila}, {columna})")

                            # ---Esto verifica si la nave fu hundida---
                            for nave in coordenadas_naves:
                                if all(coordenada in aciertos for coordenada in nave):
                                    puntaje += len(nave) * 10  # ---Le suma el puntaje adicional por haber hundido la nave---
                                    sonido_hundido.play()
                                    agregar_mensaje(f"Nave hundida! +{len(nave)*10} puntos")  # Agregar mensaje de hundimiento
                                    print(f"Nave hundida! +{len(nave)*10} puntos")
                                    coordenadas_naves.remove(nave)  # ---Borra la nave hundida---

                        else:  
                            intentos[fila][columna] = -1
                            puntaje -= 1 #---Le resta uno si da en el agua---
                            sonido_fallo.play()
                            agregar_mensaje(f"Fallo en ({fila}, {columna})") 
                            print(f"Fallo en ({fila}, {columna})")

                
                if 600 <= x <= 750 and 500 <= y <= 550:  
                    reiniciar_juego(tamano_matriz, nivel)
                elif 600 <= x <= 750 and 300 <= y <= 400:
                    pantalla_inicio()
                elif 600 <= x <= 750 and 440 <= y <= 490: 
                    pygame.quit()
                    sys.exit()

        # ---Verifica si hundieron todas las naves o si se clikearon todos los casilleros---
        if len(coordenadas_naves) == 0 or casillas_clicadas == total_casillas:
            guardar_puntaje(pedir_nombre(puntaje, pantalla), puntaje)  
            reiniciar_juego(tamano_matriz, nivel)  

        
        pantalla.fill(BLANCO) 
        mostrar_puntaje(puntaje)  
        dibujar_tablero(matriz, intentos, tamano_matriz)  
        mostrar_mensajes() 
        dibujar_boton("Salir", 600, 440, 150, 50, (200, 0, 0), NEGRO)  
        dibujar_boton("Reiniciar", 600, 500, 150, 50, (200, 200, 0), NEGRO)  
        dibujar_boton("Inicio", 600, 300, 150, 50, (180, 200, 120), NEGRO)  
        pygame.display.flip() 






pantalla_inicio()