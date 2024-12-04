import pygame
from src.home import Home
from src.view import View
from src.kana import Kana

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.myview = View()
    self.myhome = Home()
    self.kana = Kana()
    
    #self.kana = Kana() Put image in parathese
    self.inventory =[]
    self.npc = []
    
  def mainloop(self):
    #select state loop
    run = True
    while run:
      
      for event in self.myview.events():
        if event.type == pygame.QUIT:
          print("quit")
          self.myview.quit()
        if event.type == pygame.KEYDOWN: #Checks that whether a key is pressed.
          if event.key == pygame.K_SPACE: # renders new area if spacebar is pressed
            self.myhome.render_main()   
            self.myhome.render_player()
            pygame.display.flip()
            pygame.time.wait(1000)
          
      
          
            

      self.myview.render_main()


     
      
  
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