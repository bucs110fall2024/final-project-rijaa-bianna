import sys
import pygame
from src.food import Food
from src.kana import Kana

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode((400,400))
    self.background = pygame.image.load("template_final_project-master/assets/map.jpeg")
    self.background = pygame.transform.scale(self.background, self.screen.get_size())
    
    #textbox
  
    # Fill background
    self.box = pygame.Surface(self.textbox.get_size())
    self.box = self.textbox.convert()
    self.box.fill((250, 250, 250)) # these are colors, size is determined by self.texbox
    self.start_game = True

    # Display some text
    self.font = pygame.font.Font(None, 36)
    text = self.font.render("Hello there, my name is Kana. Help me collect food to feed my cat. Press space to continue", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = self.box.get_rect().centerx
    self.box.blit(text, textpos)


    #Put food here
    self.width, self.height = self.screen.get_size()
    self.friedrice = Food("template_final_project-master/assets/friedrice.png", self.width,self.height)
    
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
    print(self.x,self.y)
    #select state loop
    run = True
    while run:
      # Blit everything to the screen
      print("here 1")
      # if self.start_game == True:
      #   self.textbox.blit(self.box, (0, 0))
      #   pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          print("quit")
          self.quit()
        if event.type == pygame.KEYDOWN: #Checks that whether a key is pressed.
          if event.key == pygame.K_SPACE: # renders new area if spacebar is pressed
            self.show_player = True 
            self.start_game = False # displays our food and stops displaying the texbox
          if event.key == pygame.K_q: # renders new area if spacebar is pressed
            self.show_player = False 
          if event.key == pygame.K_DOWN:
            self.kana.move_down()
            
          if event.key == pygame.K_UP:
            self.kana.move_up()
            
          if event.key == pygame.K_LEFT:
            self.kana.move_left()
            
          if event.key == pygame.K_RIGHT:
            self.kana.move_right()
      print("here 2")
      self.render_main() 
      if self.show_player == True:  
        self.screen.blit(self.kana.img, self.kana.rect)
        self.screen.blit(self.friedrice.img, self.friedrice.rect)
        
      print("here 3")
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