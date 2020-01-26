import pygame

import math 
import random

pygame.init()
width, height = 800,  600
backgroundColor = 0,  0, 0

screen = pygame.display.set_mode((800, 600))

#Icons made by <a href="https://www.flaticon.com/authors/skyclick" title="Skyclick">Skyclick</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

enemyImg = []
enemyX = []
enemyX_change = []
enemyY = []
enemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(64, 200))
    enemyX_change.append(6)
    enemyY_change.append(50)

#Icons made by <a href="https://www.flaticon.com/authors/darius-dan" title="Darius Dan">Darius Dan</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletX_change = 0
bulletY = 480
bulletY_change = 10
bullet_state = "hold"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 38)

textX = 730
testY = 10

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def display_score(x, y):
    score = font.render("score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (400, 300))
  
def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
def Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


run = True

while run:
	screen.fill(backgroundColor)
  
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
             
             
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
                playerX_change = -5
      if event.key == pygame.K_RIGHT:
                playerX_change = 5
      if event.key == pygame.K_SPACE:
         bulletX = playerX
         bullet_fire(bulletX, bulletY)

if event.type == pygame.KEYUP:
   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
      playerX_change = 0
playerX += playerX_change
    if playerX <= 10:
        playerX = 10
    elif playerX >= 730:
        playerX = 730

for i in range(num_of_enemies):
  if enemyY[i] > 450:
      for j in range(num_of_enemies):
        enemyY[j] = 10000
        game_over_text()
        break

enemyX[i] += enemyX_change[i]
  if enemyX[i] <= 10:
      enemyX_change[i] = 10
      enemyY[i] += enemyY_change[i]
  elif enemyX[i] >= 730:
      enemyX_change[i] = -10
      enemyY[i] += enemyY_change[i]


collision = Collision(enemyX[i], enemyY[i], bulletX, bulletY)
   if collision:
      bulletY = 480
      bullet_state = "hold"
      score_value += 1
      enemyX[i] = random.randint(0, 730)
      enemyY[i] = random.randint(50, 150)
      enemy(enemyX[i], enemyY[i], i)


if bulletY <= 0:
        bulletY = 480
        bullet_state = "hold"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()