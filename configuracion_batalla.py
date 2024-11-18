import pygame
import random
import sys


# Definir el tamaño de la pantalla
ANCHO = 800
ALTO = 600
tamano_celda = 30

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Batalla Naval")
pygame.mixer.init()

pygame.mixer.music.set_volume(0.15)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Cargar imagen de fondo
fondo = pygame.image.load('imagenes/fondo.jpg')  
fondo_nivel = pygame.image.load('imagenes/fondo1.jpg') 

fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


sonido_acierto = pygame.mixer.Sound('sonidos/disparo.mp3')
sonido_fallo = pygame.mixer.Sound('sonidos/agua.mp3')
sonido_hundido = pygame.mixer.Sound('sonidos/hundido.mp3')
pygame.mixer.music.load('sonidos/fondo.mp3')
pygame.mixer.music.play(-1, 0.0)