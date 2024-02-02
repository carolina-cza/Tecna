import pygame

pygame.init()
window = pygame.display.set_mode((250,250))

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255, 0,0)

width = 20
height = 20
margin = 5

grid = []
for row in range(6):
    grid.append([])
    for column in range(6):
        grid[row].append(0)

grid[1][5] = 1

clock = pygame.time.Clock()

#main loop
while not False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] //(width + margin)
            row = pos[1] // (height + margin)
            #Set location to one
            grid[row][column] = 1
            print("Click", pos, "Grid coordinates: ", row, column)
    window.fill(black)

    #draw the grid
    for row in range(6):
        for column in range(6):
            color = white
            if grid[row] [column] == 1:
                color = green
            pygame.draw.rect(window,color,[(margin + width)* column + margin, (margin + height)* row + margin,width,height])

    clock.tick(60)

    pygame.display.flip()

    pygame.quit()


        