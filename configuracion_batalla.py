import pygame


# ---define configuracion  de la pantalla y celda---
ANCHO = 800
ALTO = 600
tamano_celda = 30
pantalla = pygame.display.set_mode((ANCHO, ALTO))


# --- define configuracion de la musica ---
music_on = True
pygame.mixer.init()
pygame.mixer.music.set_volume(0.15)
sonido_acierto = pygame.mixer.Sound('sonidos/disparo.mp3')
sonido_fallo = pygame.mixer.Sound('sonidos/agua.mp3')
sonido_hundido = pygame.mixer.Sound('sonidos/hundido.mp3')
pygame.mixer.music.load('sonidos/fondo.mp3')
pygame.mixer.music.play(-1, 0.0)


# --- Titulo del Juego ---
pygame.display.set_caption("Batalla Naval")


# ---colores---
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
color_base = (100, 149, 237)  # Color verde para todos los botones
color_texto = BLANCO  # Color blanco para el texto



# ---Cargar imagenes---
fondo = pygame.image.load('imagenes/fondo.jpg')  
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_nivel = pygame.image.load('imagenes/fondo1.jpg') 



