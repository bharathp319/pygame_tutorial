# importing pygame library
import pygame

#                            (Width, height)
win = pygame.display.set_mode((480, 600))
# create's a window for our game

#initializing pygame window and it's function
pygame.init()

# creating a variable which tell us wheather game is running or not
run = True

while run:

    # capture all event in the window
    for event in pygame.event.get():

        #if event is close the window
        if event.type == pygame.QUIT:

            #stop running 
            run = False
    # Rectangle     (window, color,   (x, y, w, h),  wide)
    pygame.draw.rect(win, (255, 0, 0), (100, 100, 50, 100), 0)

    # Circle         (window, color,  (center point), radius, wide)
    pygame.draw.circle(win, (0, 255, 0), (300, 300), 100, 5)

    # Line          (window, color,    (x1, y1),(x2, y2), wide)
    pygame.draw.line(win, (0, 0, 255), (0, 60), (300, 400), 5)

    # Polygon       (window,   color,   iscolsed,             [list of points],           wide)
    pygame.draw.lines(win, (255, 255, 0), False, [(10, 50), (100, 50), (100, 300), (10, 300)], 5)

    #update the window
    pygame.display.update()

pygame.quit()
#destroy the window
