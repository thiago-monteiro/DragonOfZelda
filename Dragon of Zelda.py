import pygame
import time
from Colorize import *
from Colors import *
from Sword import *
from Key import *

pygame.init()
pygame.font.init()

screenSize = [700, 500]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Dragon of Zelda')

done = False
clock = pygame.time.Clock()

gamestate = "DRAGON"
gObs = [0 for x in range(5)]

dragonObs = [0 for x in range(5)]
animObs = [0 for x in range(5)]
imageObs = [0 for x in range(5)]
gamestateARRAY = [0 for x in range(5)]
bulletARRAY = [0 for x in range(5)]
wallObs = [0 for x in range(40)]
swordObs = [0 for x in range(5)]

keyARRAY = [0 for x in range(10)]

gamestateARRAY[0] = gamestate

EnemyARRAY = [0 for x in range(5)]

background = pygame.image.load("Background.png").convert_alpha()
background = pygame.transform.scale(background, (700, 500))
dragon1 = pygame.image.load("HUMADRAGON.png").convert_alpha()
dragon2 = pygame.image.load("HUMADRAGON2.png").convert_alpha()
dragon1_hurt = colorize(dragon1, (255, 0, 0))
dragon2_hurt = colorize(dragon2, (255, 0, 0))

robo1 = pygame.image.load("Robot_frameA.png").convert_alpha()
robo1 = pygame.transform.scale(robo1, (175, 200))

bullet = pygame.image.load("bullet.png").convert_alpha()

sword_attack = pygame.image.load("Sword_attack.png").convert_alpha()
sword_attack_left = pygame.transform.rotate(sword_attack, -180)

robo_hurt1 = colorize(robo1, (255, 0, 0))


key_list = pygame.image.load("Key_list.png")
key_list = pygame.transform.scale(key_list, (120, 30))

dragon_sprite = 0

frame_counter = 0

animObs[0] = frame_counter

imageObs[0] = dragon1
imageObs[1] = dragon2

win_lose_font = pygame.font.SysFont('Courier New', 60)

class Empty:
    def __init__(self):
        self.name = "EMPTY"
        self.xPos = 0
        self.yPos = 0
        self.width = 0
        self.height = 0

class Robot():
    def __init__(self, xPos, yPos, width, height):
        self.name = "PLAYER"
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.health = 10
        self.hurt = False
        self.hurt_timer = 60
        self.swordamage = 5
        self.dashleft = False
        self.dashdown = False
        self.dashup = False
        self.dashright = False
        self.dashspeed = 30

        self.keys = 0

        unhurt_imageA = pygame.image.load("Robot_frameA.png").convert_alpha()
        unhurt_imageA = pygame.transform.scale(unhurt_imageA, (175, 200))

        hurt_imageA = colorize(unhurt_imageA, (255, 0, 0))

        self.image = unhurt_imageA

class Bullet():
    def __init__(self, xPos, yPos, width, height):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.name = "PLAYERBULLET"
        self.bulletdamage = 2
        self.fired = False


class Enemy():
    def __init__(self, xPos, yPos, width, height, image):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.image = image


class AnimatedEnemy():
    def __init__(self, xPos, yPos, width, height):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.name = "DRAGON"
        self.health = 50
        self.attackdamage = 2
        self.hurt = False
        self.hurt_timer = 125
        self.hurt = False

class RectangleParent():
    def __init__(self, color, xPosition, yPosition, width, height):
        self.color = color
        self.color = color
        self.xPos = xPosition
        self.yPos = yPosition
        self.width = width
        self.height = height

    def function(self):
        print("This isa message inside the TestEnemy class.")

class Wall():
    def __init__(self, color, xPosition, yPosition):
        self.color = color
        self.xPos = xPosition
        self.yPos = yPosition
        self.width = 64
        self.height = 64

leftPaddle = RectangleParent(WHITE, 20, 220, 20, 100)

for x in range(0, 6):
    wall1 = Wall(GRAY, x * 64, 64)
    wallObs[x] = wall1

dragonprime = AnimatedEnemy(400, 400, 60, 123)

dragonObs[0] = dragonprime

key01 = key(20, 32)
key02 = key(650, 350)
key03 = key(325, 175)

keyARRAY[0] = key01
keyARRAY[1] = key02
keyARRAY[2] = key03

bullet1 = Bullet(200, 269, 10, 10)
robot1 = Robot(75, 200, 100, 100)

gObs[0] = robot1

sword1 = Sword(200, 200, False)
sword2 = SwordAttack(gObs[0].xPos, gObs[0].yPos + 65, False)
swordObs[0] = sword1
swordObs[1] = sword2

bulletARRAY[0] = bullet1

rect_x = 75
rect_y = 75
rectSizeA = 35
rectSizeB = 15

rect_change_x = 1.7
rect_change_y = 1.7

def detectCollision(targetA, targetB):
    if targetA.xPos < targetB.xPos + targetB.width and targetA.xPos + targetA.width > targetB.xPos and targetA.yPos < targetB.yPos + targetB.height and targetA.height + targetA.yPos > targetB.yPos:
        if targetA.name == "PLAYERSWORD" and targetB.name == "DRAGON":
            dragonObs[0].hurt = True
            dragonObs[0].health = dragonObs[0].health - swordObs[0].attackdamage

        if targetA.name == "SWORD_ATTACK" and targetB.name == "DRAGON":
            dragonObs[0].hurt = True
            dragonObs[0].health = dragonObs[0].health - swordObs[0].attackdamage
            swordObs[0].attacking = False

        if targetA.name == "PLAYER" and targetB.name == "KEY":
            gObs[0].keys = gObs[0].keys + 1
            targetB.name = "EMPTY"

        if targetA.name == "PLAYER" and targetB.name == "SWORD":
            swordObs[0].equipped = True
            targetB.name = "PLAYERSWORD"

        if targetA.name == "PLAYER" and targetB.name == "DRAGON":
            if targetA.hurt == False:
                targetA.health -= targetB.attackdamage
                targetA.hurt = True

        if targetA.name == "PLAYERBULLET" and targetB.name == "DRAGON":
            if bulletARRAY[0].fired:
                dragonObs[0].hurt = True
                dragonObs[0].health = dragonObs[0].health - bulletARRAY[0].bulletdamage


def update():

    if swordObs[0].equipped:
        swordObs[1].yPos = gObs[0].yPos + 60
        swordObs[1].xPos = gObs[0].xPos - 45
        
    detectCollision(gObs[0], keyARRAY[0])
    detectCollision(gObs[0], keyARRAY[1])
    detectCollision(gObs[0], keyARRAY[2])
    detectCollision(bulletARRAY[0], dragonObs[0])
    detectCollision(gObs[0], swordObs[0])
    detectCollision(gObs[0], dragonObs[0])

    if swordObs[0].attacking:
        detectCollision(swordObs[1], dragonObs[0])

    if (gObs[0].hurt_timer < 1):
        gObs[0].hurt = False
        gObs[0].hurt_timer = 60
    else:
        if gObs[0].hurt:
            gObs[0].hurt_timer -= 1

    if (dragonObs[0].hurt_timer < 1):
        dragonObs[0].hurt = False
        dragonObs[0].hurt_timer = 125

    else:
        if dragonObs[0].hurt:
            dragonObs[0].hurt_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                if swordObs[0].counter > 0:
                    swordObs[0].attacking = True

            if event.key == pygame.K_w:
                gObs[0].dashup = True
            if event.key == pygame.K_d:
                gObs[0].dashright = True
            if event.key == pygame.K_a:
                gObs[0].dashleft = True
            if event.key == pygame.K_s:
                gObs[0].dashdown = True
            if event.key == pygame.K_SPACE:
                bulletARRAY[0].fired = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                gObs[0].dashup = False
            if event.key == pygame.K_d:
                gObs[0].dashright = False
            if event.key == pygame.K_a:
                gObs[0].dashleft = False
            if event.key == pygame.K_s:
                gObs[0].dashdown = False
            if event.key == pygame.K_KP_ENTER:
                swordObs[0].attacking = False

        if gObs[0].dashup == True:
            gObs[0].yPos = gObs[0].yPos - gObs[0].dashspeed

        if gObs[0].dashdown == True:
            gObs[0].yPos = gObs[0].yPos + gObs[0].dashspeed
        
        if gObs[0].dashright == True:
            gObs[0].xPos = gObs[0].xPos + gObs[0].dashspeed

        if gObs[0].dashleft == True:
            gObs[0].xPos -= gObs[0].dashspeed
    
    if bulletARRAY[0].xPos > 700 or dragonObs[0].hurt:
        bulletARRAY[0].xPos2 = gObs[0].xPos + 120
        bulletARRAY[0].yPos2 = gObs[0].yPos + 70
        bulletARRAY[0].xPos = bulletARRAY[0].xPos2
        bulletARRAY[0].yPos = bulletARRAY[0].yPos2
        bulletARRAY[0].fired = False

    if bulletARRAY[0].fired == True:
        bulletARRAY[0].xPos = bulletARRAY[0].xPos + 10

    if animObs[0] <= 30:
        animObs[0] += 1
    else:
        animObs[0] = 0

while not done:

    update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if gamestateARRAY[0] == "DRAGON":
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        if swordObs[0].equipped == False:
            screen.blit(swordObs[0].image, (swordObs[0].xPos, swordObs[0].yPos))

        else:

            if swordObs[0].attacking == False:
                screen.blit(swordObs[0].image, (gObs[0].xPos, gObs[0].yPos))
            else:
                screen.blit(swordObs[1].image, (swordObs[1].xPos, swordObs[1].yPos))

        if animObs[0] <= 15:
            if dragonObs[0].hurt:
                screen.blit(dragon1_hurt, (dragonObs[0].xPos, dragonObs[0].yPos))
            else:
                screen.blit(dragon1, (dragonObs[0].xPos, dragonObs[0].yPos))
            
            if gObs[0].hurt:
                screen.blit(robo_hurt1, (gObs[0].xPos, gObs[0].yPos))
            else:
                screen.blit(robo1, (gObs[0].xPos, gObs[0].yPos))
        else:
            if dragonObs[0].hurt:
                screen.blit(dragon2_hurt, (dragonObs[0].xPos, dragonObs[0].yPos))

            else:
                screen.blit(dragon2, (dragonObs[0].xPos, dragonObs[0].yPos))

            if gObs[0].hurt:
                screen.blit(robo_hurt1, (gObs[0].xPos, gObs[0].yPos))
            else:
                screen.blit(robo1, (gObs[0].xPos, gObs[0].yPos))
                
        # screen.blit(bullet, (gObs[0].xPos, gObs[0].yPos))
        pygame.draw.rect(screen, BLACK, [0, 0, 700, 40])
        screen.blit(key_list, (20, 5))

        if gObs[0].keys == 3 and dragonObs[0].health == 0:
            text = win_lose_font.render("You Win!", True, (230, 200, 0))
            screen.blit(text, (200, 200))
            pygame.display.flip()
            time.sleep(1)
            pygame.display.flip()
            break

        if keyARRAY[0].name == "KEY":
            screen.blit(keyARRAY[0].image, (keyARRAY[0].xPos, keyARRAY[0].yPos))

        if keyARRAY[1].name == "KEY":
            screen.blit(keyARRAY[1].image, (keyARRAY[1].xPos, keyARRAY[1].yPos))

        if keyARRAY[2].name == "KEY":
            screen.blit(keyARRAY[2].image, (keyARRAY[2].xPos, keyARRAY[2].yPos))

        font = pygame.font.SysFont('Courier New', 30)
        text = font.render(str(gObs[0].keys), True, (230, 200, 0))
        screen.blit(text, (150, 5))
        font = pygame.font.SysFont('Courier New', 20)
        text = font.render("Current HP: " + str(gObs[0].health), True, (230, 200, 0))
        screen.blit(text, (200, 10))
        text = font.render("Dragon HP: " + str(dragonObs[0].health), True, (230, 200, 0))
        screen.blit(text, (400, 10))
            
        if gObs[0].health == 0 or dragonObs[0].health == 0:
            text = win_lose_font.render("You Lost!", True, (230, 200, 0))
            screen.blit(text, (200, 200))
            pygame.display.flip()
            time.sleep(1)
            pygame.display.flip()
            break

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
