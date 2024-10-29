import pygame, sys
pygame.init()

screen = pygame.display.set_mode([500, 500])
playerrect = pygame.Rect(10, 10, 10, 10)
wallrect = pygame.Rect(245, 0, 10, 250)
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            currentx =+ pygame.mouse.get_pos()[0]
            currenty =+ pygame.mouse.get_pos()[1]
            playerrect.update(x-5, y-5, 10, 10)
        
    
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen,[255, 255, 255],playerrect)
    pygame.draw.rect(screen,[255, 255, 255],wallrect)

    pygame.display.flip()