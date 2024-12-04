import sys
import pygame
from src.home import Home
from src.kana import Kana

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.background = pygame.image.load("template_final_project-master/assets/map.jpeg")
    self.background = pygame.transform.scale(self.background, self.screen.get_size())
    
  
    self.myhome = Home()
    self.kana = Kana()
    self.show_player = False
    #self.kana = Kana() Put image in parathese
    self.inventory =[]
    self.npc = []
  
  def render_main(self):
      self.screen.fill((0,0,0))
      self.screen.blit(self.background, (0,0)) #Draws one surface on top of another surface
        
  def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
      
  def mainloop(self):
    #select state loop
    run = True
    while run:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          print("quit")
          self.quit()
        if event.type == pygame.KEYDOWN: #Checks that whether a key is pressed.
          if event.key == pygame.K_SPACE: # renders new area if spacebar is pressed
            self.show_player = True 
          if event.key == pygame.K_q: # renders new area if spacebar is pressed
            self.show_player = False 
      
      if self.show_player == True:  
        self.screen.blit(self.kana.img, (0,0))
      else:
        self.render_main() 
        
      pygame.display.flip()


     
      
  
  ### below are some sample loop states ###

  def menuloop(self):
      pass
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw