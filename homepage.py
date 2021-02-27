import pygame
pygame.init()

mode = 0
screen = pygame.display.set_mode([1080, 620])
run = True
background = pygame.image.load('Background.jpg')
bg2 = pygame.transform.scale(background, (1280, 620))
badbutton1 = pygame.image.load('CodeDay Feb 2021 Button.png')
goodbutton1 = pygame.transform.scale(badbutton1, (282, 93))
badbutton2 = pygame.image.load('CodeDay Feb 2021 Button 2.png')
goodbutton2 = pygame.transform.scale(badbutton2, (282, 93))
logo1 = pygame.image.load('Spacescape logo.png')
logo2 = pygame.transform.scale(logo1, (784, 346))

level = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 689 > pos[0] > 409 and 451 > pos[1] > 363:
                mode = 1
                print(mode)
            if 687 > pos[0] > 409 and 581 > pos[1] > 493:
                mode = 2
                print(mode)

    screen.fill((255, 255, 255))
    screen.blit(bg2, (-100, 0))
    screen.blit(goodbutton1, (408, 360))
    screen.blit(goodbutton2, (408, 490))
    screen.blit(logo2, (138, -10))

    pygame.display.flip()
pygame.quit()