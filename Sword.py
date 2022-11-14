import pygame


class SwordAttack:
    def __init__(self, xPos, yPos, equipped):
        self.name = "SWORD_ATTACK"
        self.attackdamage = 5
        self.xPos = xPos
        self.yPos = yPos
        self.width = 74
        self.height = 24
        self.equipped = equipped
        self.attacking = False
        self.counter = 30
        self.visible = False

        sword_attack_image = pygame.image.load("Sword_attack.png").convert_alpha()
        self.image = sword_attack_image

class Sword:

    def __init__(self, xPos, yPos, equipped):
        self.name = "SWORD"

        self.attackdamage = 5
        self.xPos = xPos
        self.yPos = yPos
        self.width = 20
        self.height = 89
        self.equipped = equipped
        self.attacking = False
        self.counter = 30
        self.visible = False

        sword_image = pygame.image.load("Sword.png").convert_alpha()
        self.image = sword_image



