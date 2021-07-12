import pygame
import random
import math

#score





#initialise the game
pygame.init()

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
over_font = pygame.font.Font('freesansbold.ttf',64)
textX = 10
textY = 10

#gameover text


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (32, 178, 170))
    screen.blit(over_text, (200, 250)),

def show_score(x,y):
    score = font.render("Score:"+str(score_value) + "                         STAY HOME STAY SAFE",True,(32,178,170))
    screen.blit(score, (x, y))

#create the screen
screen = pygame.display.set_mode((800,600))

#title and ICON
pygame.display.set_caption("Corona Invaders")
icon = pygame.image.load('doctor.png')
pygame.display.set_icon(icon)

#player


playerimg = pygame.image.load('vaccine.png').convert_alpha()
playerimg = pygame.transform.smoothscale(playerimg, (64, 64))
playerX = 370
playery = 480
playerx_change = 0

#enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg = pygame.image.load('virus.png').convert_alpha()
    enemyImg = pygame.transform.smoothscale(enemyImg, (64, 64))
    enemyimg.append(enemyImg)
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(0.3)
    enemyy_change.append(40)




#Bullet
Bulletimg = pygame.image.load('drop.png').convert_alpha()
Bulletimg = pygame.transform.smoothscale(Bulletimg, (32, 32))
Bulletx = 0
Bullety = 480
Bulletx_change = 0
Bullety_change = 5
bullet_state = "ready"

#background

bg = pygame.image.load('hospital.jpg').convert_alpha()
bg = pygame.transform.smoothscale(bg, (800, 600))





def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bulltet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(Bulletimg,(x+16,y+10))

def isCollision(enemyx,enemyy,BulletX,Bullety):
    distance = math.sqrt((math.pow(enemyx-BulletX,2)) + (math.pow(enemyy-Bullety,2)))

    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))
     #background image
    screen.blit(bg,(0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
                print("Left arrows is pressed")
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
                print("right arrows is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    Bulletx = playerX
                    fire_bulltet(Bulletx,Bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
                print("Key stroke has been released")




    playerX += playerx_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    for i in range (num_of_enemies):

        #Game over

        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]

        if enemyx[i] <= 0:
            enemyx_change[i] = 0.3
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.3
            enemyy[i] += enemyy_change[i]

            # collision
        collison = isCollision(enemyx[i], enemyy[i], Bulletx, Bullety)
        if collison:
            Bullety = 480
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
            print(score_value)
        enemy(enemyx[i], enemyy[i] , i)
        #Bullet movement

    if Bullety <=0:
        Bullety = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bulltet(Bulletx,Bullety)
        Bullety -= Bullety_change



    player(playerX,playery)
    show_score(textX,textY)

    pygame.display.update()