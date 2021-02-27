import pygame
import random

screen = pygame.display.set_mode([1366, 768])

pygame.init()

# caption and Icon
pygame.display.set_caption("Spacecape")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# background
backgroundImg = pygame.image.load("Background.jpg")
background = pygame.transform.scale(backgroundImg, (1700, 768))

# Player
playerImg1 = pygame.image.load('player.png')
player_right = pygame.transform.scale(playerImg1, (128, 128))
playerImg = player_right
player_left = pygame.transform.flip(playerImg, True, False)

playerX = 555
playerY = 600
playerX_change = 0

asteroidImg1 = pygame.image.load('asteroid.png')
asteroidImg = []
asteroidX = []
asteroidY = []
asteroidY_change = []
num_of_asteroids = 3

explosionImg1 = pygame.image.load('explosion.png')
explosionImg = pygame.transform.scale(explosionImg1, (256, 256))

for i in range(num_of_asteroids):
    asteroidImg.append(pygame.transform.scale(asteroidImg1, (100, 100)))
    asteroidX.append(random.randint(0, 1238))
    asteroidY.append(random.randint(0, 150))
    asteroidY_change.append(random.randint(2, 6) / 10)


def player(x, y):
    screen.blit(playerImg, (x, y))


def asteroid(x, y, i):
    screen.blit(asteroidImg[i], (x, y))


def explosion(x, y, i):
    screen.blit(explosionImg, (x, y))


running = True

while running:

    screen.fill((255, 255, 255))
    screen.blit(background, (-100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerImg = player_left
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerImg = player_right
                playerX_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1238:
        playerX = 1238

    # Enemy movement
    for i in range(num_of_asteroids):
        asteroid(asteroidX[i], asteroidY[i], i)
        asteroidY[i] += asteroidY_change[i]

        # Game over
        if asteroidY[i] > 528:
            explosion(asteroidX[i], 450, i)
            break

    player(playerX, playerY)
    pygame.display.update()