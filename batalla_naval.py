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

# Cargar imagen de fondo
fondo = pygame.image.load('fondo.jpg')  # Asegúrate de tener una imagen llamada 'fondo.jpg'
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

fondo_nivel = pygame.image.load('fondo1.jpg')  # Asegúrate de tener una imagen llamada 'fondo.jpg'
fondo_nivel = pygame.transform.scale(fondo, (ANCHO, ALTO))


# Función para mostrar un texto en la pantalla
def mostrar_texto(texto, color, x, y):
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))

# Función para dibujar un botón
def dibujar_boton(texto, x, y, ancho, alto, color_boton, color_texto):
    pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto))
    mostrar_texto(texto, color_texto, x + 20, y + 20)  # Ajuste de posición del texto en el botón

# Función para mostrar la pantalla de inicio
def pantalla_inicio():
    while True:
        pantalla.blit(fondo, (0, 0))  # Mostrar el fondo
        mostrar_texto("Batalla Naval", NEGRO, 300, 50)  # Título de la pantalla
        
        # Dibujar botones
        dibujar_boton("Nivel", 300, 150, 200, 50, (0, 200, 0), BLANCO)
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
                if 300 <= x <= 500 and 150 <= y <= 200:  # Botón "Nivel"
                    print("Seleccionar Nivel")
                    pantalla_seleccion_nivel()  # Llamamos a la pantalla de selección de nivel
                elif 300 <= x <= 500 and 220 <= y <= 270:  # Botón "Jugar"
                    print("Iniciar Juego")
                    pantalla_seleccion_nivel()  # Llamamos a la pantalla de selección de nivel
                elif 300 <= x <= 500 and 290 <= y <= 340:  # Botón "Ver Puntajes"
                    print("Ver Puntajes")
                    # Aquí iría la lógica para ver los puntajes
                elif 300 <= x <= 500 and 360 <= y <= 410:  # Botón "Salir"
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()  # Actualizar la pantalla
        pygame.time.Clock().tick(60)  # 60 FPS

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
                    iniciar_juego(10)  # Llamar a la función para iniciar el juego con tablero de 10x10
                    corriendo = False
                elif 300 <= x <= 500 and 220 <= y <= 270:  # Botón "Medio"
                    print("Nivel Medio seleccionado")
                    iniciar_juego(20)  # Llamar a la función para iniciar el juego con tablero de 20x20
                    corriendo = False
                elif 300 <= x <= 500 and 290 <= y <= 340:  # Botón "Difícil"
                    print("Nivel Difícil seleccionado")
                    iniciar_juego(40)  # Llamar a la función para iniciar el juego con tablero de 40x40
                    corriendo = False
        
        pygame.display.flip()  # Actualizar la pantalla


# Función para iniciar el juego con el tamaño de la matriz
def iniciar_juego(tamano_matriz):
    print(f"Iniciando juego con tablero de tamaño {tamano_matriz}x{tamano_matriz}")
    matriz = crear_matriz(tamano_matriz)
    poner_naves(matriz)
    
    # Bucle principal del juego
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar el tablero
        pantalla.fill(BLANCO)
        dibujar_tablero(matriz, tamano_matriz)
        pygame.display.flip()

# Función para crear la matriz de 10x10
def crear_matriz(tamano_matriz):
    # Creamos una matriz de tamaño dinámico con todas las celdas inicializadas en 0 (agua)
    matriz = [[0 for _ in range(tamano_matriz)] for _ in range(tamano_matriz)]
    return matriz

# Función para colocar las naves de forma aleatoria en el tablero
def poner_naves(matriz):
    tamano_matriz = len(matriz)

    # Definir la cantidad de cada tipo de nave y su tamaño (submarino: 1, destructor: 2, crucero: 3, acorazado: 4)
    tipos_naves = {
        "submarino": 1,   # 4 submarinos de 1 casillero
        "destructor": 2,   # 3 destructores de 2 casilleros
        "crucero": 3,      # 2 cruceros de 3 casilleros
        "acorazado": 4     # 1 acorazado de 4 casilleros
    }

 # Función auxiliar para verificar si la nave cabe en la matriz y no se solapa
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

    # Función auxiliar para colocar una nave en la matriz
    def colocar_nave(fila, columna, longitud, direccion):
        if direccion == 'horizontal':
            for i in range(longitud):
                matriz[fila][columna + i] = 1  # Marcar cada celda como ocupada por la nave
        elif direccion == 'vertical':
            for i in range(longitud):
                matriz[fila + i][columna] = 1  # Marcar cada celda como ocupada por la nave

    # Colocar las naves de forma aleatoria
    for tipo, longitud in tipos_naves.items():
        cantidad = 0

        # Colocar naves según el tipo
        while cantidad < (4 if tipo == "submarino" else (3 if tipo == "destructor" else (2 if tipo == "crucero" else 1))):
            fila = random.randint(0, tamano_matriz - 1)
            columna = random.randint(0, tamano_matriz - 1)
            direccion = random.choice(['horizontal', 'vertical'])

            # Verificar si la nave cabe en la posición aleatoria
            if verificar_posicion(fila, columna, longitud, direccion):
                colocar_nave(fila, columna, longitud, direccion)
                cantidad += 1

def dibujar_tablero(matriz, tamano_matriz):
    # Calculamos el tamaño máximo de la celda para que se ajuste a la pantalla
    tamano_celda = min(ANCHO, ALTO) // tamano_matriz  # Esto asegura que las celdas no excedan el tamaño de la pantalla
    for fila in range(tamano_matriz):
        for columna in range(tamano_matriz):
            color = BLANCO if matriz[fila][columna] == 0 else (0, 200, 0)  # Si no hay nave, dibuja blanco; si hay nave, verde
            pygame.draw.rect(pantalla, color, (columna * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda))
            pygame.draw.rect(pantalla, NEGRO, (columna * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda), 2)  # Dibujar bordes de las celdas



# Función para colocar las naves de forma aleatoria en el tablero
def poner_naves(matriz):
    tamano_matriz = len(matriz)
    cantidad_naves = tamano_matriz  # Podemos ajustar este número según el nivel de dificultad

    for _ in range(cantidad_naves):
        fila = random.randint(0, tamano_matriz - 1)
        columna = random.randint(0, tamano_matriz - 1)
        # Verificar si ya hay una nave en esa posición
        while matriz[fila][columna] == 1:
            fila = random.randint(0, tamano_matriz - 1)
            columna = random.randint(0, tamano_matriz - 1)
        matriz[fila][columna] = 1  # Colocar nave en la posición aleatoria

# Ejecutar la pantalla de inicio
pantalla_inicio()
