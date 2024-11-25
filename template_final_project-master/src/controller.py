import pygame
from src.kana import Kana

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    self.background = pygame.image.load("assets/map.jpeg")
    
    #self.kana = Kana() Put image in parathese
    self.inventory =[]
    self.npc = []
    
  def mainloop(self):
    #select state loop
    run = True
    while run:
      for event in pygame.event.get():
        pass
      
      self.screen.blit(self.background, (0,0))
      pygame.display.flip() #RESIZE USING TRANSFORM
  
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
