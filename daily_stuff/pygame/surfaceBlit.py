import pygame
import time

pygame.init()

sample_surface = pygame.display.set_mode((400,300))

color = (255,255,0)

pygame.draw.rect(sample_surface,color,pygame.Rect(30,70,90,90))

pygame.display.flip()

status = True

while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
            pygame.quit()
