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

    # --- Crea la matriz y definicion de variable principales ---
    matriz = crear_matriz(tamano_matriz) #--- matriz donde estan las naves ---
    intentos = crear_matriz(tamano_matriz)# --- matriz para los intentos ----
    puntaje = 0
    aciertos = []
    mensajes.clear()


    # ---segun el nivel seleccionado , se coloca las naves y la cantidad ---
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
    total_casillas = tamano_matriz * tamano_matriz #---calcula tamano de la matriz ---

    
    while corriendo:
        for evento in pygame.event.get(): #---recorre los eventos del juego ---
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if evento.type == pygame.MOUSEBUTTONDOWN:# --- cuando hace click , obtiene la posicion del mouse
                x, y = pygame.mouse.get_pos()     
                fila, columna = y // tamano_celda, x // tamano_celda # ---calcula la celda seleccionada en la matrizcon el mouse---
                if 0 <= fila < tamano_matriz and 0 <= columna < tamano_matriz: # ---cheque que las coordenadas entan dentro de los limites de la matriz---
                    if intentos[fila][columna] == 0:  # ---Verifica si la celda se clickeo antes---
                        casillas_clicadas += 1  
                        # --- si el jugador acierta ---
                        if matriz[fila][columna] == 1:  
                            intentos[fila][columna] = 1 #---se marca con un 1 ---
                            puntaje += 5
                            aciertos.append((fila, columna))  # ---guarda si le pegamos a la neave---
                            sonido_acierto.play()
                            agregar_mensaje(f"Acierto en ({fila}, {columna})") 
                            print(f"Acierto en ({fila}, {columna})")

                            # ---esto verifica si la nave fu hundida---
                            for nave in coordenadas_naves:
                                nave_hundida = True
                                for coordenada in nave:
                                    if coordenada not in aciertos:
                                        nave_hundida = False
                                        break  # ---si alguna coordenada no está en aciertos, termina el bucle---
                                if nave_hundida:
                                    puntaje += len(nave) * 10  # Le suma el puntaje adicional por haber hundido la nave
                                    sonido_hundido.play()
                                    agregar_mensaje(f"Nave hundida! +{len(nave)*10}")  # Agregar mensaje de hundimiento
                                    print(f"Nave hundida! +{len(nave)*10}")
                                    coordenadas_naves.remove(nave)  # Borra la nave hundida
                        else:  
                            intentos[fila][columna] = -1 # --- marca el intento como fallo ---
                            puntaje -= 1 #---Le resta uno si da en el agua---
                            sonido_fallo.play()
                            agregar_mensaje(f"Fallo en ({fila}, {columna})") 
                            print(f"Fallo en ({fila}, {columna})")

                # ---Verificar si se hace clic en el botón de reiniciar---
                if 600 <= x <= 750 and 500 <= y <= 550:  
 
                    puntaje = 0
                    intentos = crear_matriz(tamano_matriz)  # --- Reiniciar la matriz de intentos ---
                    aciertos = []  # --- vuelve los valores a 0 ---
                       
                    matriz = crear_matriz(tamano_matriz) # Limpia las coordenadas de las naves para evitar duplicación
                    coordenadas_naves.clear() 
                    coordenadas_naves = poner_naves(matriz, naves)  # Reponer las naves
                    agregar_mensaje("Juego reiniciado!")  # Mensaje de confirmación
                    print("Juego reiniciado")
                    mensajes.clear()

                # ---Verificar si se hace clic en el botón de inicio---
                elif 600 <= x <= 750 and 300 <= y <= 400:
                    mostrar_pantalla("inicio")  # Volver a la pantalla de inicio
                elif 600 <= x <= 750 and 440 <= y <= 490: 
                    pygame.quit()
                    sys.exit()

          
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # --- Calcular el estado hover para cada botón --- 
        hover_salir = 600 <= mouse_x <= 750 and 440 <= mouse_y <= 490
        hover_reiniciar = 600 <= mouse_x <= 750 and 500 <= mouse_y <= 550
        hover_inicio = 600 <= mouse_x <= 750 and 300 <= mouse_y <= 400

        # ---Verifica si hundieron todas las naves o si se clikearon todos los casilleros---
        if len(coordenadas_naves) == 0 or casillas_clicadas == total_casillas:
            guardar_puntaje(pedir_nombre(puntaje, pantalla), puntaje)  
            mostrar_pantalla("inicio")
 

        
        pantalla.fill(BLANCO) 
        dibujar_tablero(matriz, intentos, tamano_matriz)  
        mostrar_puntaje(puntaje)  
        mostrar_mensajes() 
        # Dibujar los botones con efecto hover
        dibujar_boton("Salir", 625, 440, 150, 50, (135, 206, 235), NEGRO, hover=hover_salir)  
        dibujar_boton("Reiniciar", 625, 500, 150, 50, (135, 206, 235), NEGRO, hover=hover_reiniciar)  
        dibujar_boton("Inicio", 625, 300, 150, 50, (135, 206, 235), NEGRO, hover=hover_inicio)
 
        pygame.display.flip() # --- actualiza la pantalla ---





def mostrar_pantalla(tipo_pantalla:str, nivel_predeterminado:str="fácil", music_on:bool=True)->None:
    """
    Función: Muestra  la interfaz gráfica del juego
    Parámetros: Tipo de pantalla que se debe mostrar (por defecto en facil)
    music_on : Por defecto, está activada.
    Retorno: None: Esta función no devuelve ningún valor
    """
    corriendo = True # --- Variable para mantener el juego activo ---

    
    while corriendo:
                # --- Cargar fondo diferente para la pantalla de selección de nivel---
        if tipo_pantalla == "seleccion_nivel":
            fondo_seleccion_nivel = pygame.transform.scale(pygame.image.load('imagenes/fondo3.jpg'), (ANCHO, ALTO))
            pantalla.blit(fondo_seleccion_nivel, (0, 0))
        else:
            pantalla.blit(fondo, (0, 0))  # ---dibuja ondo por defecto--- 

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if tipo_pantalla == "inicio":
            
            mostrar_texto("Batalla Naval", NEGRO, 330, 50)
            #             texto       coordenadas y tamanio   color de fondo     color    condicion del mouse , si es verdadera
            #                                del boton         del boton         texto             aplica el hover
            dibujar_boton("Nivel",     300, 140, 200, 60,     (171, 116, 0),      NEGRO, hover=300 <= mouse_x <= 500 and 140 <= mouse_y <= 200)
            dibujar_boton("Jugar", 300, 220, 200, 50, (171, 116, 0), NEGRO, hover=300 <= mouse_x <= 500 and 220 <= mouse_y <= 270)
            dibujar_boton("Ver Puntajes", 300, 290, 200, 50, (171, 116, 0), NEGRO, hover=300 <= mouse_x <= 500 and 290 <= mouse_y <= 340)
            dibujar_boton("Salir", 300, 360, 200, 50, (171, 116, 0), NEGRO, hover=300 <= mouse_x <= 500 and 360 <= mouse_y <= 410)

           
            texto_musica = "Música: On" if music_on else "Música: Off"
            hover_texto_musica = 0 <= mouse_x <= 200 and 0 <= mouse_y <= 50
            dibujar_boton( texto_musica, 0 ,0, 200, 50, (0, 128, 0), BLANCO,hover=hover_texto_musica  )

        elif tipo_pantalla == "seleccion_nivel":
            dibujar_boton("Fácil", 300, 150, 200, 50, (155, 249, 0 ), NEGRO, hover=300 <= mouse_x <= 500 and 150 <= mouse_y <= 200)
            dibujar_boton("Medio", 300, 220, 200, 50,(215, 209, 1 ), NEGRO, hover=300 <= mouse_x <= 500 and 220 <= mouse_y <= 270)
            dibujar_boton("Difícil", 300, 290, 200, 50,(252, 64, 64)    , NEGRO, hover=300 <= mouse_x <= 500 and 290 <= mouse_y <= 340)
    

        for evento in pygame.event.get(): # --- recorre los eventos del juego ---
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN: #--- cuando se hace click , se obtiene la posicion del mouse ---
                x, y = pygame.mouse.get_pos() 
                # --- depende donde se clikea (diferentes botones), realiza diferentes acciones 
                if tipo_pantalla == "inicio":      
                    if 300 <= x <= 500 and 140 <= y <= 200:
                        mostrar_pantalla("seleccion_nivel", nivel_predeterminado, music_on)       
                    elif 300 <= x <= 500 and 220 <= y <= 270:
                        iniciar_juego(10, nivel=nivel_predeterminado)
                        corriendo = False                       
                    elif 300 <= x <= 500 and 290 <= y <= 340:
                        mostrar_pantalla_puntajes(pantalla)                      
                    elif 300 <= x <= 500 and 360 <= y <= 410:
                        pygame.quit()
                        sys.exit()
              
                    elif 0 <= x <= 200 and 0 <= y <= 50:
                        music_on = not music_on
                        if music_on:
                            pygame.mixer.music.play(-1, 0.0)
                        else:
                            pygame.mixer.music.stop()

                elif tipo_pantalla == "seleccion_nivel":  
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




mostrar_pantalla("inicio")

mostrar_pantalla("seleccion_nivel")

