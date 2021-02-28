import pygame
import random
import time

screen = pygame.display.set_mode([1080, 620])

pygame.init()

# caption and Icon
pygame.display.set_caption("Spacecape")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# background
backgroundImg = pygame.image.load("Background.jpg")
background = pygame.transform.scale(backgroundImg, (1380, 620))

# Player
playerImg1 = pygame.image.load('player.png')
player_right = pygame.transform.scale(playerImg1, (128, 128))
playerImg = player_right
player_left = pygame.transform.flip(playerImg, True, False)

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
asteroidY_change.append(random.randint(20, 30) / 10)


def player(x, y):
    screen.blit(playerImg, (x, y))
    return


def asteroid(x, y):
    screen.blit(asteroidImg, (x, y))
    return


def explosion(x, y):
    screen.blit(explosionImg, (x, y))
    return


def death():
    print("Game Over")
    return


running = True
direction = False
shottime = 0
while running:
    screen.blit(background, (-100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerImg = player_left
                direction = False
                playerX_change = -2.4
            if event.key == pygame.K_RIGHT:
                playerImg = player_right
                direction = True
                playerX_change = 2.4
            if event.key == pygame.K_SPACE:
                if time.time() - shottime > 0.5:
                    print("shot")
                    screen.blit(bulletright if direction else bulletleft,
                                (playerX + 128 if direction else playerX - 30, 550))
                    bullets.append([direction, playerX + 128 if direction else playerX - 30])
                    shottime = time.time()
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
            if x[1] >= 1080:
                bullets.remove(x)
            else:
                screen.blit(bulletright if x[0] else bulletleft, (x[1] + 30 if x[0] else x[1] - 30, 550))
                x[1] = x[1] + 30 if x[0] else x[1] - 30
    player(playerX, playerY)
    pygame.display.update()
