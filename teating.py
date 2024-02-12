import pygame

pygame.init()

windowWidth = 500
windowHeight = 500

display = pygame.display.set_mode((windowWidth,windowHeight))
font = pygame.font.Font("freesansbold.ttf",24)

#game variable
game_start = False

# o
while True :
    pygame.display.set_caption("Start Menu")
    display.fill((243,217,177))
    start_text = font.render("Play",True,(255,255,255))
    display.blit(start_text,(200,200))

    #check if space is pressed
    if game_start == True:
        main()
    else:
        start_text


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                True
        if event .type == pygame.QUIT:
            False
    pygame.display.update()

    pygame.quit()
                