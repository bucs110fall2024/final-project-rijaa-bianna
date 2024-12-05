import pygame
from src.food import Food

class Kana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        '''
        initializes kana player image
        '''
        self.img= pygame.image.load("template_final_project-master/assets/characters/kanaclose.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (60,60))
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 100
    

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed
