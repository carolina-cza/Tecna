import pygame

pygame.init()
window = pygame.display.set_mode((400,450))

#def colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255, 0,0)

#def width and hight of each grid location
width = 55
height = 55
margin = 5

#create a 2 dimensional array
grid = []
for row in range(4):
    grid.append([])
    for column in range(4):
        grid[row].append(0)

#set row 1, cell 5 to one
#grid[1][2] = 1

clock = pygame.time.Clock()

#Loop until the user clicks the close button
done = False

#main loop
while not done:
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked close
            done = True      #exit this loop  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #user clicks the mouse + get the position
            pos = pygame.mouse.get_pos()
            #change the x/y screen coordinates to grid coordinates
            column = pos[0] //(width + margin)
            row = pos[1] // (height + margin)
            #Set location to one
            grid[row][column] = 1
            print("Click", pos, "Grid coordinates: ", row, column)
    window.fill(black)

    #draw the grid
    for row in range(4):
        for column in range(4):
            color = white
            if grid[row] [column] == 1:
                color = red
            pygame.draw.rect(window,
                             color,
                             [(margin + width)* column + margin,
                               (margin + height)* row + margin,
                               width,
                               height])  

    clock.tick(60)

    pygame.display.flip()

pygame.quit()


        