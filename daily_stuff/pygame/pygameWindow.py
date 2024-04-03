import pygame

pygame.init()

#define the background colour, using RGB color coding
background_colour = (255,51,255)

#define dimensions of screen object
screen = pygame.display.set_mode((400,400),pygame.RESIZABLE)

#set the caption of the screen
pygame.display.set_caption('HelloWorld')

#fill the background colour to the screen
screen.fill(background_colour)

#update the display using flip
pygame.display.flip()

#variable to keep our game loop running
running = True

#game loop
while running:

    for event in pygame.event.get():
        #check for quit event
        if event.type == pygame.QUIT:
            running = False

#quit pygame after closing window
            pygame.quit()