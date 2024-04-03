import pygame

pygame.init()

X = 450
Y = 700

background_colour = (255,51,255)

screen = pygame.display.set_mode((X,Y))

pygame.display.set_caption('image')

imp = pygame.image.load("C:\\Users\\CzaplaC\\Python\\images\\casper.jpg").convert()

screen.blit(imp,(0,0))

font = pygame.font.SysFont("Comic Sans MS",44)
text =font.render("Hey ich bin Casper^^",True, (188,172,144))
textRec = text.get_rect()
textRec.center = (250,670)
screen.blit(text,textRec)

pygame.display.flip()

status = True

while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
            pygame.quit()