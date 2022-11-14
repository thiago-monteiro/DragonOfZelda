import pygame


class key:
    def __init__(self, xPos, yPos):
        self.name = "KEY"
        self.xPos = xPos
        self.yPos = yPos
        self.width = 30
        self.height = 75
        small_key = pygame.image.load("small_key.png")
        self.image = small_key