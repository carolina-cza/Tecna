import pygame

pygame.font.init()
pygame.font.get_init()

display_surface = pygame.display.set_mode((500,500))

pygame.display.set_caption('Text')

font1 = pygame.font.SysFont("freesanbold.ttf",50)
text1 = font1.render("Hello World",True, (0,225,0))
textRect1 = text1.get_rect()
textRect1.center= (250,250)

while True:
    display_surface.fill((255,0,0))

    display_surface.blit(text1, textRect1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            quit()
        pygame.display.update()

