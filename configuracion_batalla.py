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


# ---Cargar imagenes---
fondo = pygame.image.load('imagenes/fondo.jpg')  
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_nivel = pygame.image.load('imagenes/fondo1.jpg') 
fondo_agua=pygame.image.load('imagenes/fondo juego.png') 
imagen_victoria=pygame.image.load('imagenes/fondo_victoria.png') 
imagen_victoria = pygame.transform.scale(imagen_victoria, (ANCHO, ALTO))



# ---Cargar imagenes---
fondo = pygame.image.load('imagenes/fondo.jpg')  
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_nivel = pygame.image.load('imagenes/fondo1.jpg') 







