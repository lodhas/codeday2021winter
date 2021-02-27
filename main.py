import pygame
pygame.init()


screen = pygame.display.set_mode([500, 500])
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 100)
    pygame.display.flip()
pygame.quit()
