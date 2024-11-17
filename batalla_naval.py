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

# Inicializar pygame
pygame.init()

# Definir el tamaño de la pantalla
ANCHO = 800
ALTO = 600
tamano_celda = 30
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Batalla Naval")

# Fuentes
fuente = pygame.font.SysFont('Arial', 36)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
puntaje = 0 
# Cargar imagen de fondo
fondo = pygame.image.load('fondo.jpg')  # Asegúrate de tener una imagen llamada 'fondo.jpg'
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

fondo_nivel = pygame.image.load('fondo1.jpg')  # Asegúrate de tener una imagen llamada 'fondo.jpg'



# Función para mostrar un texto en la pantalla
def mostrar_texto(texto, color, x, y):
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))

# Función para dibujar un botón
def dibujar_boton(texto, x, y, ancho, alto, color_boton, color_texto):
    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto))
    mostrar_texto(texto, color_texto, x + 20, y + 20)  # Ajuste de posición del texto en el botón



def mostrar_puntaje(puntaje):
    fuente = pygame.font.SysFont("Arial", 36)  # Fuente y tamaño del texto
    texto = fuente.render(f"Puntaje: {puntaje:04d}", True, NEGRO)  # Formato 0000
    pantalla.blit(texto, (600, 10))  # Dibuja el texto en la esquina superior izquierda
   

# Función para mostrar la pantalla de inicio
def pantalla_inicio():
    nivel_predeterminado = "fácil"  # Nivel predeterminado si el jugador no selecciona otro nivel

    while True:
        pantalla.blit(fondo, (0, 0))  # Mostrar el fondo
        mostrar_texto("Batalla Naval", NEGRO, 300, 50)  # Título de la pantalla

        # Dibujar botones
        dibujar_boton("Nivel", 300, 140, 200, 60, (150, 0, 200), BLANCO)
        dibujar_boton("Jugar", 300, 220, 200, 50, (0, 0, 200), BLANCO)
        dibujar_boton("Ver Puntajes", 300, 290, 200, 50, (200, 0, 0), BLANCO)
        dibujar_boton("Salir", 300, 360, 200, 50, (200, 200, 0), BLANCO)

        # Verificar eventos (clic en los botones)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener posición del ratón
                x, y = pygame.mouse.get_pos()

                # Verificar si se hizo clic en algún botón
                if 300 <= x <= 500 and 140 <= y <= 200:  # Botón "Nivel"
                    print("Seleccionar Nivel")
                    pantalla_seleccion_nivel()  # Llamar a la pantalla de selección de nivel
                elif 300 <= x <= 500 and 220 <= y <= 270:  # Botón "Jugar"
                    print("Iniciar Juego")
                    iniciar_juego(10, nivel=nivel_predeterminado)  # Inicia el juego directamente
                elif 300 <= x <= 500 and 290 <= y <= 340:  # Botón "Ver Puntajes"
                    print("Ver Puntajes")
                    pantalla_puntajes()  # Llamar a la función para ver los puntajes
                elif 300 <= x <= 500 and 360 <= y <= 410:  # Botón "Salir"
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()  # Actualizar la pantalla

      

# Función para mostrar la pantalla de selección de nivel
def pantalla_seleccion_nivel():
    corriendo = True
    
    # Cargar la imagen de fondo
    fondo = pygame.image.load('fondo1.jpg')  # Asegúrate de tener la imagen en el directorio adecuado
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))  # Ajusta el tamaño de la imagen al tamaño de la pantalla
    
    while corriendo:
        pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla
        mostrar_texto("Selecciona el Nivel", NEGRO, 270, 50)  # Título de la pantalla
        
        # Dibujar botones de nivel
        dibujar_boton("Fácil", 300, 150, 200, 50, (0, 200, 0), BLANCO)
        dibujar_boton("Medio", 300, 220, 200, 50, (0, 0, 200), BLANCO)
        dibujar_boton("Difícil", 300, 290, 200, 50, (200, 0, 0), BLANCO)
        
        # Verificar eventos (clic en los botones)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener posición del ratón
                x, y = pygame.mouse.get_pos()
                
                # Verificar si se hizo clic en algún botón de nivel
                if 300 <= x <= 500 and 150 <= y <= 200:  # Botón "Fácil"
                    print("Nivel Fácil seleccionado")
                    iniciar_juego(10, nivel="fácil")  # Llamar a la función para iniciar el juego con tablero de 10x10
                    corriendo = False
                elif 300 <= x <= 500 and 220 <= y <= 270:  # Botón "Medio"
                    print("Nivel Medio seleccionado")
                    iniciar_juego(20, nivel="medio")  # Llamar a la función para iniciar el juego con tablero de 20x20
                    corriendo = False
                elif 300 <= x <= 500 and 290 <= y <= 340:  # Botón "Difícil"
                    print("Nivel Difícil seleccionado")
                    iniciar_juego(40, nivel="difícil")  # Llamar a la función para iniciar el juego con tablero de 40x40
                    corriendo = False
        
        pygame.display.flip()  # Actualizar la pantalla
 
# Función para mostrar la pantalla de puntajes
def pantalla_puntajes():
    corriendo = True
    while corriendo:
        pantalla.fill(BLANCO)
        mostrar_texto("Puntajes", NEGRO, 300, 50)
        
        # Aquí podrías cargar y mostrar los puntajes desde un archivo o variable
        mostrar_texto("Puntaje Máximo: 0000", NEGRO, 300, 150)
        
        # Dibujar botón para regresar al menú
        dibujar_boton("Volver", 300, 360, 200, 50, (200, 200, 0), NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 <= x <= 500 and 360 <= y <= 410:  # Botón "Volver"
                    corriendo = False
        
        pygame.display.flip()



# Definir la función crear_matriz para crear un tablero de tamaño tamano_matriz x tamano_matriz
def crear_matriz(tamano_matriz):
    return [[0 for _ in range(tamano_matriz)] for _ in range(tamano_matriz)]

# El resto de tu código sigue igual...


def iniciar_juego(tamano_matriz, nivel="fácil"):
    print(f"Iniciando juego con tablero de tamaño {tamano_matriz}x{tamano_matriz} y nivel {nivel}")
    matriz = crear_matriz(tamano_matriz)
    intentos = crear_matriz(tamano_matriz)  # Matriz para registrar los intentos del jugador (-1: fallo, 1: acierto)
    puntaje = 0
    aciertos = []
    
    # Configurar las naves según el nivel
    if nivel == "medio":
        naves = [("acorazado", 4, 2), ("crucero", 3, 4), ("destructor", 2, 6), ("submarino", 1, 8)]
    elif nivel == "difícil":
        naves = [("acorazado", 4, 3), ("crucero", 3, 6), ("destructor", 2, 9), ("submarino", 1, 12)]
    else:
        naves = [("acorazado", 4, 1), ("crucero", 3, 2), ("destructor", 2, 3), ("submarino", 1, 4)]

    # Crear las coordenadas de las naves en la matriz
    coordenadas_naves = poner_naves(matriz, naves)
    
    tamano_celda = min(ANCHO, ALTO) // tamano_matriz
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Detectar clic en el tablero
                fila, columna = y // tamano_celda, x // tamano_celda
                if 0 <= fila < tamano_matriz and 0 <= columna < tamano_matriz:
                    if intentos[fila][columna] == 0:  # Solo registrar si no ha sido clicado antes
                        if matriz[fila][columna] == 1:  # Acierto
                            intentos[fila][columna] = 1
                            puntaje += 5
                            aciertos.append((fila, columna))  # Registrar el acierto
                            print(f"Acierto en ({fila}, {columna})")
                            
                            # Verificar si alguna nave ha sido hundida
                            for nave in coordenadas_naves:
                                if all(coordenada in aciertos for coordenada in nave):
                                    puntaje += len(nave) * 10  # 10 puntos por cada elemento de la nave
                                    print(f"Nave hundida! +{len(nave)*10} puntos")
                                    coordenadas_naves.remove(nave)  # Eliminar la nave hundida de la lista

                        else:  # Fallo
                            intentos[fila][columna] = -1
                            puntaje -= 1
                            print(f"Fallo en ({fila}, {columna})")
                
                # Detectar clic en botones
                if 600 <= x <= 750 and 500 <= y <= 550:  # Reiniciar
                    iniciar_juego(tamano_matriz, nivel)
                elif 600 <= x <= 750 and 440 <= y <= 490:  # Salir
                    pygame.quit()
                    sys.exit()

        pantalla.fill(BLANCO)
        mostrar_puntaje(puntaje) 
        dibujar_tablero(matriz, intentos, tamano_matriz)
        dibujar_boton("Salir", 600, 440, 150, 50, (200, 0, 0), NEGRO)
        dibujar_boton("Reiniciar", 600, 500, 150, 50, (200, 200, 0), NEGRO)
        pygame.display.flip()



# Función para colocar las naves de forma aleatoria en el tablero
def poner_naves(matriz, naves):
    tamano_matriz = len(matriz)
    coordenadas_naves = []  # Lista para guardar las coordenadas de las naves

    # Iterar sobre las naves
    for nave in naves:
        nombre, largo, cantidad = nave

        # Intentar colocar las naves en el tablero
        for _ in range(cantidad):  # Para cada nave de este tipo
            colocada = False  # Bandera para saber si se logró colocar la nave

            while not colocada:
                # Determinar si la nave será colocada horizontal o verticalmente
                orientacion = random.choice(["horizontal", "vertical"])

                # Elegir una posición aleatoria en el tablero
                fila = random.randint(0, tamano_matriz - 1)
                columna = random.randint(0, tamano_matriz - 1)

                # Verificar si la nave cabe en la posición elegida sin solaparse
                if orientacion == "horizontal":
                    if columna + largo <= tamano_matriz:  # Verificar si cabe horizontalmente
                        # Comprobar si las celdas están vacías
                        if all(matriz[fila][columna + i] == 0 for i in range(largo)):
                            # Colocar la nave
                            for i in range(largo):
                                matriz[fila][columna + i] = 1  # Marcar las celdas ocupadas
                            coordenadas_naves.append([(fila, columna + i) for i in range(largo)])  # Guardar las coordenadas
                            colocada = True  # Nave colocada con éxito

                else:  # Colocación vertical
                    if fila + largo <= tamano_matriz:  # Verificar si cabe verticalmente
                        # Comprobar si las celdas están vacías
                        if all(matriz[fila + i][columna] == 0 for i in range(largo)):
                            # Colocar la nave
                            for i in range(largo):
                                matriz[fila + i][columna] = 1  # Marcar las celdas ocupadas
                            coordenadas_naves.append([(fila + i, columna) for i in range(largo)])  # Guardar las coordenadas
                            colocada = True  # Nave colocada con éxito

    return coordenadas_naves


        # Función auxiliar para verificar si la nave cabe y no se solapan
    def verificar_posicion(fila, columna, longitud, direccion):
        if direccion == 'horizontal':
            if columna + longitud > tamano_matriz:  # Verificar si la nave cabe en el tablero horizontalmente
                return False
            # Verificar si las celdas están vacías
            for i in range(longitud):
                if matriz[fila][columna + i] != 0:
                    return False
        elif direccion == 'vertical':
            if fila + longitud > tamano_matriz:  # Verificar si la nave cabe en el tablero verticalmente
                return False
            # Verificar si las celdas están vacías
            for i in range(longitud):
                if matriz[fila + i][columna] != 0:
                    return False
        return True

    # Función auxiliar para colocar la nave en la matriz
    def colocar_nave(fila, columna, longitud, direccion):
        if direccion == 'horizontal':
            for i in range(longitud):
                matriz[fila][columna + i] = 1  # Marcar la celda como ocupada
        elif direccion == 'vertical':
            for i in range(longitud):
                matriz[fila + i][columna] = 1  # Marcar la celda como ocupada

    # Colocar las naves en el tablero
    for tipo, longitud, cantidad in naves:
        for _ in range(cantidad):
            nave_colocada = False
            while not nave_colocada:
                fila = random.randint(0, tamano_matriz - 1)
                columna = random.randint(0, tamano_matriz - 1)
                direccion = random.choice(['horizontal', 'vertical'])
                
                if verificar_posicion(fila, columna, longitud, direccion):
                    colocar_nave(fila, columna, longitud, direccion)
                    nave_colocada = True


def dibujar_tablero(matriz, intentos, tamano_matriz):
    tamano_celda = min(ANCHO, ALTO) // tamano_matriz
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            color = BLANCO if matriz[fila][columna] == 0 else (0, 200, 0)
            pygame.draw.rect(pantalla, color, (columna * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda))
            pygame.draw.rect(pantalla, NEGRO, (columna * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda), 2)

            # Dibujar marcas según los intentos
            if intentos[fila][columna] == 1:  # Acierto
                pygame.draw.line(pantalla, (255, 0, 0), 
                                 (columna * tamano_celda, fila * tamano_celda),
                                 ((columna + 1) * tamano_celda, (fila + 1) * tamano_celda), 3)
                pygame.draw.line(pantalla, (255, 0, 0), 
                                 ((columna + 1) * tamano_celda, fila * tamano_celda),
                                 (columna * tamano_celda, (fila + 1) * tamano_celda), 3)
            elif intentos[fila][columna] == -1:  # Fallo
                pygame.draw.circle(pantalla, (0, 0, 255), 
                                   (columna * tamano_celda + tamano_celda // 2, 
                                    fila * tamano_celda + tamano_celda // 2), tamano_celda // 3, 2)





# Ejecutar la pantalla de inicio
pantalla_inicio()