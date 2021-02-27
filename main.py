import pygame


pygame.init()


# caption and Icon
pygame.display.set_caption("DA GAME")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode([1080, 720])
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    pygame.display.flip()
pygame.quit()