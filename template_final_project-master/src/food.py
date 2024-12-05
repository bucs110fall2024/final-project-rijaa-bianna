import pygame
import sys
<<<<<<< HEAD
from src.kana import Kana
class Food():
    def __init__(self, img):
        super().__init__()
        
        self.img= pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (60,60))
        self.rect = self.img.get_rect()
        
        
        
=======
#from src.kana import Kana
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, image, screensize_x, screensize_y):
        super().__init__()
        '''
        initializes food image
        '''
        self.image_show = image
        self.img= pygame.image.load(self.image_show).convert_alpha()
        self.img = pygame.transform.scale(self.img, (60,60))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0,screensize_x- self.rect.width)
        self.rect.y = random.randint(0,screensize_y - self.rect.height)
>>>>>>> 378300b02640f74c47c7a03407e099c547bfdfef
        
    def events(self):
        return pygame.event.get() #Makes events, need it for the for loop to check if player made a keyboard commad\
    
    def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
        
      
        
        