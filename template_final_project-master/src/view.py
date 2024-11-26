import pygame
import sys
class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.image.load("template_final_project-master/assets/map.jpeg")
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        
    def render_main(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (0,0)) #Draws one surface on top of another surface
      
        
        pygame.display.flip() #doesnn't display anything until the program internally loads everything (displays eveyrthing at once). Call it only once every frame
    
    def events(self):
        return pygame.event.get() #Makes events, need it for the for loop to check if player made a keyboard commad\
    
    def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
    
    