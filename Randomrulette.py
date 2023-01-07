import pygame
import random

# Inicializamos pygame
pygame.init()

# Lista de elementos
elementos = ['manzana', 'plátano', 'pera']

# Seleccionamos un elemento aleatorio de la lista
elegido = random.choice(elementos)

# Creamos una ventana de 400x400 pixels
ventana = pygame.display.set_mode((400, 400))

# Dibujamos la ruleta en la pantalla
pygame.draw.circle(ventana, (0, 0, 0), (200, 200), 150)

# Dibujamos el elemento elegido en la pantalla
texto = font.render(elegido, True, (255, 255, 255))
ventana.blit(texto, (200, 200))

# Actualizamos la pantalla
pygame.display.flip()

# Esperamos a que el usuario cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
