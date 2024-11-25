import pygame

class Kana(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        
        self.img= pygame.image.load("")
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 1
    
    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed
