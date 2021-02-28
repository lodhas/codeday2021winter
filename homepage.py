import pygame

pygame.init()

mode = 0
screen = pygame.display.set_mode([1080, 620])
run = True
background = pygame.image.load('Background.jpg')
bg2 = pygame.transform.scale(background, (1280, 620))
badbutton1 = pygame.image.load('CodeDay Feb 2021 Button.png')
goodbutton1 = pygame.transform.scale(badbutton1, (282, 93))
#badbutton2 = pygame.image.load('CodeDay Feb 2021 Button 2.png')
#goodbutton2 = pygame.transform.scale(badbutton2, (282, 93))
logo1 = pygame.image.load('Spacescape logo.png')
logo2 = pygame.transform.scale(logo1, (784, 346))
helpicon1 = pygame.image.load('Help Icon.png')
helpicon2 = pygame.transform.scale(helpicon1, (544, 246))

status = 0

def help():
    thing = True
    helptext = pygame.image.load('Help Text.png')
    ht2 = pygame.transform.scale(helptext, (1080, 620))
    screen.blit(ht2, (0, 0))
    print("Salutations")
    global status
    status = 1
    return

def unhelp():
    screen.fill((255, 255, 255))
    screen.blit(bg2, (-100, 0))
    screen.blit(goodbutton1, (408, 360))
    #screen.blit(goodbutton2, (408, 490))
    screen.blit(logo2, (138, -10))
    screen.blit(helpicon2, (750, -70))
    global status
    status = 0
    return

unhelp()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 689 > pos[0] > 409 and 451 > pos[1] > 363 and status == 0:
                mode = 1
                print(mode)
            if 1058 > pos[0] > 975 and 85 > pos[1] > 11 and status == 0:
                mode = 3
                help()
                pygame.display.flip()
                print(mode)
            if 1068 > pos[0] > 744 and 612 > pos[1] > 525 and status == 1:
                print("Go to homepage")
                unhelp()
            else:
                print(pos)

    pygame.display.flip()
pygame.quit()
