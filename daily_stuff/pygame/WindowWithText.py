import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode([800,500])

#basic font for user
base_font = pygame.font.Font(None,32)
user_text = "Input here: "

#create rectangle
input_rect = pygame.Rect(200,200,140,32)

color_active = pygame.Color('lightskyblue3')

color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

while True: 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            #check for backspace
            if event.key == pygame.K_BACKSPACE:

            #get text input from 0 to -1 i.e end.
                user_text = user_text[:-1]
            
            #unicode standard is used for string formation
            else:
                user_text += event.unicode
                #if text_surface.get_width() > input_rect.w -400:
                   # user_text = user_text[:-1]
    
    display.fill((255,255, 255))

    if active:
        color = color_active
    else:
        color = color_passive

    #draw rectangle and argument passed which should be on screen
    pygame.draw.rect(display,color, input_rect)

    text_surface = base_font.render(user_text, True, (255,255,255))

    #render at position stated in arguments
    display.blit(text_surface,(input_rect.x+5, input_rect.y+10))

    #set width of textfield so that text cannot get outside of users text input
    input_rect.w = max(100,text_surface.get_width()+10)

    pygame.display.flip()

    clock.tick(60)
