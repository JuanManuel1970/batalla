from funciones_batalla import *
from configuracion_batalla import *
import pygame
import sys


pygame.init()


def iniciar_juego(tamano_matriz:int, nivel:str="fácil")->None:
    """
    Funcion : Inicia el juego de Batalla Naval, creando y mostrando la matriz del tablero

    Parámetros: El tamaño de la matriz del tablero del juego

    Retorno: None. Esta función no devuelve ningún valor
    """

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

                # ---Verificar si se hace clic en el botón de reiniciar---
                if 600 <= x <= 750 and 500 <= y <= 550:  
                    # Aquí reiniciamos el puntaje y otros parámetros sin cambiar la pantalla
                    puntaje = 0
                    intentos = crear_matriz(tamano_matriz)  # Reiniciar la matriz de intentos
                    aciertos = []  # Reiniciar los aciertos
                        # Limpiar las coordenadas de las naves para evitar duplicación
                    matriz = crear_matriz(tamano_matriz)
                    coordenadas_naves.clear() 
                    coordenadas_naves = poner_naves(matriz, naves)  # Reponer las naves
                    agregar_mensaje("Juego reiniciado!")  # Mensaje de confirmación
                    print("Juego reiniciado")

                # ---Verificar si se hace clic en el botón de inicio---
                elif 600 <= x <= 750 and 300 <= y <= 400:
                    mostrar_pantalla("inicio")  # Volver a la pantalla de inicio
                elif 600 <= x <= 750 and 440 <= y <= 490: 
                    pygame.quit()
                    sys.exit()

            # Obtener las coordenadas del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calcular el estado hover para cada botón
        hover_salir = 600 <= mouse_x <= 750 and 440 <= mouse_y <= 490
        hover_reiniciar = 600 <= mouse_x <= 750 and 500 <= mouse_y <= 550
        hover_inicio = 600 <= mouse_x <= 750 and 300 <= mouse_y <= 400

        # ---Verifica si hundieron todas las naves o si se clikearon todos los casilleros---
        if len(coordenadas_naves) == 0 or casillas_clicadas == total_casillas:
            guardar_puntaje(pedir_nombre(puntaje, pantalla), puntaje)  
            mostrar_pantalla("inicio")
 

        
        pantalla.fill(BLANCO) 
        mostrar_puntaje(puntaje)  
        dibujar_tablero(matriz, intentos, tamano_matriz)  
        mostrar_mensajes() 
        # Dibujar los botones con efecto hover
        dibujar_boton("Salir", 600, 440, 150, 50, (200, 0, 0), NEGRO, hover=hover_salir)  
        dibujar_boton("Reiniciar", 600, 500, 150, 50, color_base, color_texto, hover=hover_reiniciar)  
        dibujar_boton("Inicio", 600, 300, 150, 50, color_base, color_texto, hover=hover_inicio)
 
        pygame.display.flip() 





def mostrar_pantalla(tipo_pantalla:str, nivel_predeterminado:str="fácil", music_on:bool=True)->None:
    """
    Función: Muestra  la interfaz gráfica del juego
    Parámetros: Tipo de pantalla que se debe mostrar (por defecto en facil)
    music_on (bool): Por defecto, está activada.
    Retorno: None: Esta función no devuelve ningún valor
    """
    corriendo = True
    fondo = pygame.image.load('imagenes/fondo1.jpg')
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    
    while corriendo:
        pantalla.blit(fondo, (0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if tipo_pantalla == "inicio":
            mostrar_texto("Batalla Naval", NEGRO, 300, 50)
 
            dibujar_boton("Nivel", 300, 140, 200, 60, color_base, color_texto, hover=300 <= mouse_x <= 500 and 140 <= mouse_y <= 200)
            dibujar_boton("Jugar", 300, 220, 200, 50, color_base, color_texto, hover=300 <= mouse_x <= 500 and 220 <= mouse_y <= 270)
            dibujar_boton("Ver Puntajes", 300, 290, 200, 50, color_base, color_texto, hover=300 <= mouse_x <= 500 and 290 <= mouse_y <= 340)
            dibujar_boton("Salir", 300, 360, 200, 50, (200, 0, 0), NEGRO, hover=300 <= mouse_x <= 500 and 360 <= mouse_y <= 410)

            # Mostrar el botón de música con "On" o "Off"
            texto_musica = "Música: On" if music_on else "Música: Off"
            # Definir la condición de hover para el botón "texto_musica"
            hover_texto_musica = 0 <= mouse_x <= 200 and 0 <= mouse_y <= 50
            # Dibujar el botón de música en la posición correcta y con hover
            dibujar_boton( texto_musica, 0 ,0, 200, 50, (0, 128, 0), BLANCO,hover=hover_texto_musica  )

        elif tipo_pantalla == "seleccion_nivel":
            dibujar_boton("Fácil", 300, 150, 200, 50, color_base, BLANCO, hover=300 <= mouse_x <= 500 and 150 <= mouse_y <= 200)
            dibujar_boton("Medio", 300, 220, 200, 50,color_base, BLANCO, hover=300 <= mouse_x <= 500 and 220 <= mouse_y <= 270)
            dibujar_boton("Difícil", 300, 290, 200, 50, color_base, BLANCO, hover=300 <= mouse_x <= 500 and 290 <= mouse_y <= 340)


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # Solo se obtiene en este evento


                if tipo_pantalla == "inicio":
                    # Verificamos si se está clicando en el botón de "Nivel"
                    if 300 <= x <= 500 and 140 <= y <= 200:
                        mostrar_pantalla("seleccion_nivel", nivel_predeterminado, music_on)
                    
                    # Verificamos si se está clicando en el botón de "Jugar"
                    elif 300 <= x <= 500 and 220 <= y <= 270:
                        iniciar_juego(10, nivel=nivel_predeterminado)
                        corriendo = False
                    
                    # Verificamos si se está clicando en el botón de "Ver Puntajes"
                    elif 300 <= x <= 500 and 290 <= y <= 340:

                        mostrar_pantalla_puntajes()
                    
                    # Verificamos si se está clicando en el botón de "Salir"
                    elif 300 <= x <= 500 and 360 <= y <= 410:
                        pygame.quit()
                        sys.exit()

                    # Verificamos si se está clicando en el botón de "Música"
                    elif 0 <= x <= 200 and 0 <= y <= 50:
                        music_on = not music_on
                        if music_on:
                            pygame.mixer.music.play(-1, 0.0)
                        else:
                            pygame.mixer.music.stop()

                elif tipo_pantalla == "seleccion_nivel":
                    # Verificamos si se está clicando en el botón de "Fácil"
                    if 300 <= x <= 500 and 150 <= y <= 200:
                        iniciar_juego(10, nivel="fácil")
                        corriendo = False
                    
                    # Verificamos si se está clicando en el botón de "Medio"
                    elif 300 <= x <= 500 and 220 <= y <= 270:
                        iniciar_juego(20, nivel="medio")
                        corriendo = False
                    
                    # Verificamos si se está clicando en el botón de "Difícil"
                    elif 300 <= x <= 500 and 290 <= y <= 340:
                        iniciar_juego(40, nivel="difícil")
                        corriendo = False
        
        pygame.display.flip()




mostrar_pantalla("inicio")

mostrar_pantalla("seleccion_nivel")
