import pygame
import sys
from src.kana import Kana
class Home():
    def __init__(self):
        '''
        initializes home image
        '''
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.image.load("template_final_project-master/assets/kanahouse.png").convert()
       
        
        
    def render_main(self):
        '''
        renders background
        '''
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (625,200)) 
        
    def render_player(self):
        '''
        renders kana onto screen
        '''
        kana = Kana()
        self.screen.blit(kana.img, (0,0))
        
    def events(self):
        return pygame.event.get() #Makes events, need it for the for loop to check if player made a keyboard commad\
    
    def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
        
      
        
        