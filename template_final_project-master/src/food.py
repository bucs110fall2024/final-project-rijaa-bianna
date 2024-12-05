import pygame
import sys
from src.kana import Kana
class Food():
    def __init__(self, img):
        super().__init__()
        
        self.img= pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (60,60))
        self.rect = self.img.get_rect()
        
        
        
        
    def events(self):
        return pygame.event.get() #Makes events, need it for the for loop to check if player made a keyboard commad\
    
    def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
        
      
        
        