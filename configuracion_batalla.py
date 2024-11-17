import pygame

ANCHO = 800
ALTO = 600
tamano_celda = 30
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Batalla Naval")



#  imagen de fondo
fondo = pygame.image.load('fondo.jpg')  
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

fondo_nivel = pygame.image.load('fondo1.jpg') 
