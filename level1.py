import pygame
import random
import time

screen = pygame.display.set_mode([1080, 620])

pygame.init()

# alien death sound
oof = pygame.mixer.Sound("thetrueoof.wav")

# laser sound
laser = pygame.mixer.Sound("laser.wav")

# play again screen
play_again = pygame.image.load("Death Screen.png")
deathscreen = pygame.transform.scale(play_again, (1080, 620))

# caption and Icon
pygame.display.set_caption("SpacEscape")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# background sound
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

# background
backgroundImg = pygame.image.load("Background.jpg")
background = pygame.transform.scale(backgroundImg, (1380, 620))

# Player
playerImg1 = pygame.image.load('player.png')
player_right = pygame.transform.scale(playerImg1, (128, 128))
playerImg = player_right
player_left = pygame.transform.flip(playerImg, True, False)

# aliens
alien_starting_location = [0, 1000]
alienImg1 = pygame.image.load('alien.png')
alienImg = pygame.transform.scale(alienImg1, (80, 80))
alienX = []
alienY = 530
aliens = []
alienX_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    startloc = alien_starting_location[random.randint(0, 1)]
    if startloc == 0:
        change = random.randint(1, 2) / 10
    else:
        change = random.randint(1, 2) / -10
    aliens.append([startloc, change])

playerX = 555
playerY = 500
playerX_change = 0

asteroidImg = pygame.image.load('asteroid.png')
asteroidImg = pygame.transform.scale(asteroidImg, (100, 100))
asteroidX = []
asteroidY = []
asteroidY_change = []
explosionTime = []
explosionX = []

explosionImg1 = pygame.image.load('explosion.png')
explosionImg = pygame.transform.scale(explosionImg1, (100, 100))

bullet = pygame.image.load("bullet.png")
bulletleft = pygame.transform.rotate(bullet, 90)
bulletright = pygame.transform.rotate(bullet, -90)
bullets = []

asteroidX.append(random.randint(0, 824))
asteroidY.append(random.randint(0, 150))
asteroidY_change.append(random.randint(2, 3) / 10)

# score

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10
# Game over text

over_font = font = pygame.font.Font('freesansbold.ttf', 64)
alive = True


def getscore():
    global alive
    global deathtime
    score_value = int(((time.time() if alive else deathtime) - starttime) * 100 // 1)
    return score_value


def show_score(x, y):
    score_value = getscore()
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))
    return


def alien(x, y):
    screen.blit(alienImg, (x, y))
    return


def asteroid(x, y):
    screen.blit(asteroidImg, (x, y))
    return


def explosion(x, y):
    screen.blit(explosionImg, (x, y))
    return


def death():
    global alive
    global deathtime
    deathtime = time.time()
    print("Game Over")
    alive = False

    return


deathtime = 0
direction = False
running = False
run = True
shottime = 0

badbutton1 = pygame.image.load('CodeDay Feb 2021 Button.png')
goodbutton1 = pygame.transform.scale(badbutton1, (282, 93))
# badbutton2 = pygame.image.load('CodeDay Feb 2021 Button 2.png')
# goodbutton2 = pygame.transform.scale(badbutton2, (282, 93))
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
    screen.blit(background, (-100, 0))
    screen.blit(goodbutton1, (408, 360))
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
                status = 2
                run = False
                running = True
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
starttime = time.time()
while running:
    if alive:
        start = time.time()
        screen.blit(background, (-100, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerImg = player_left
                    direction = False
                    playerX_change = -0.6
                if event.key == pygame.K_RIGHT:
                    playerImg = player_right
                    direction = True
                    playerX_change = 0.6
                if event.key == pygame.K_SPACE:
                    if time.time() - shottime > 0.4:
                        print("shot")
                        screen.blit(bulletright if direction else bulletleft,
                                    (playerX + 128 if direction else playerX - 30, 550))
                        bullets.append([direction, playerX + 128 if direction else playerX - 30])
                        shottime = time.time()
                        pygame.mixer.Sound.play(laser)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 952:
            playerX = 952

        # Enemy movement
        i = 0
        for asteroids in asteroidX:
            # Meteor Hits
            if asteroidY[i] > 520:
                explosionX.append(asteroidX[i])
                explosionTime.append([time.time(), asteroidX[i]])
                asteroidY.remove(asteroidY[i])
                asteroidX.remove(asteroidX[i])
                i += 1
                asteroidX.append(random.randint(0, 824))
                asteroidY.append(random.randint(0, 150))
                asteroidY_change.append(random.randint(20, 30) / 10)

            else:
                asteroid(asteroidX[i], asteroidY[i])
                asteroidY[i] += asteroidY_change[i]
        for timestamp in explosionTime:
            if time.time() - timestamp[0] >= 3:
                explosionTime.remove(timestamp)
                explosionX.remove(timestamp[1])
            else:
                if timestamp[1] < playerX + 100 < timestamp[1] + 200:
                    death()
                    break
        if len(explosionX) <= 0:
            pass
        else:
            for explosions in explosionX:
                explosion(explosions, 500)
        if len(bullets) <= 0:
            pass
        else:
            for x in bullets:
                if x[1] >= 1080 or x[1] <= 0:
                    bullets.remove(x)
                else:
                    screen.blit(bulletright if x[0] else bulletleft, (x[1] + 3 if x[0] else x[1] - 3, 550))
                    x[1] = x[1] + 3 if x[0] else x[1] - 3
                for i in range(6):
                    if aliens[i][0] < x[1] < aliens[i][0] + 80:
                        pygame.mixer.Sound.play(oof)
                        aliens.remove(aliens[i])
                        bullets.remove(x)
                        startloc = alien_starting_location[random.randint(0, 1)]
                        if startloc == 0:
                            change = random.randint(1, 2) / 10
                        elif startloc == 1000:
                            change = random.randint(1, 2) / -10
                        aliens.append([startloc, change])
                        break
        for thing in aliens:
            if playerX < thing[0] < playerX + 128:
                death()
                break
        for i in range(num_of_aliens):
            alien(aliens[i][0], 530)
            aliens[i][0] += aliens[i][1]
        show_score(0, 0)
        player(playerX, playerY)
        pygame.display.update()
    else:
        screen.blit(deathscreen, (0, 0))
        score = font.render(str(getscore()), True, (255, 255, 255))
        screen.blit(score, (515, 315))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                x = pos[0]
                y = pos[1]
                if 231 < x < 910 and 415 < y < 585:
                    alive = True
                    aliens = []
                    for i in range(num_of_aliens):
                        startloc = alien_starting_location[random.randint(0, 1)]
                        if startloc == 0:
                            change = random.randint(1, 2) / 10
                        else:
                            change = random.randint(1, 2) / -10
                        aliens.append([startloc, change])
                    playerX = 555
                    playerY = 500
                    playerX_change = 0
                    asteroidX = []
                    asteroidY = []
                    asteroidY_change = []
                    explosionTime = []
                    explosionX = []
                    bullets = []
                    asteroidX.append(random.randint(0, 824))
                    asteroidY.append(random.randint(0, 150))
                    asteroidY_change.append(random.randint(2, 3) / 10)
                    starttime = time.time()
