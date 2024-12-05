import pygame
from src.food import Food

class Kana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        """
        initializes kana object
        args: self
        """
        self.img= pygame.image.load("template_final_project-master/assets/characters/kanaclose.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (60,60))
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 50
    

    def move_up(self):
        """
        moves kana up
        args: self
        """
        self.rect.y -= self.speed

    def move_down(self):
        """
        moves kana down
        args: self
        """
        self.rect.y += self.speed

    def move_right(self):
        """
        moves kana right
        args: self
        """
        self.rect.x += self.speed

    def move_left(self):
        """
        moves kana left
        args: self
        """
        self.rect.x -= self.speed
