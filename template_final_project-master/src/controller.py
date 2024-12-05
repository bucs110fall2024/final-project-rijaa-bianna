import sys
import pygame
from src.food import Food
from src.kana import Kana

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()


    self.screen = pygame.display.set_mode()
    self.dimensions = self.screen.get_size() #so we can check the dimensions of a given screen, replaced screen.get_size instances with this
    self.background = pygame.image.load("template_final_project-master/assets/map.jpeg")
    self.background = pygame.transform.scale(self.background, self.dimensions)
    
    #variables to control what shows on the screen
    self.show_player = False
    self.show_textbox = True # start game controls the textbox display
    self.show_friedrice = False
    self.show_pizza = False
    self.show_cookie = False
    
    #textbox
    self.box = pygame.Surface((self.dimensions[0] - 300, self.dimensions[1] - 100 ))
    self.box = self.box.convert()
    self.box.fill((250, 250, 250)) # these are colors, size is determined by self.texbox

    # Display some text
    self.font = pygame.font.Font(None, 36)
    text = self.font.render("Hello there, my name is Kana. Help me collect food to feed my cat. Press space to continue", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = self.box.get_rect().centerx
    self.box.blit(text, textpos)


    #Put food here
    self.friedrice = Food("template_final_project-master/assets/friedrice.png", self.dimensions[0], self.dimensions[1])
    self.pizza = Food("template_final_project-master/assets/pizza.png", self.dimensions[0], self.dimensions[1])
    #self.lassi = Food("template_final_project-master/assets/lassi.png", self.dimensions[0], self.dimensions[1])
    self.cookie = Food("template_final_project-master/assets/cookie.png", self.dimensions[0], self.dimensions[1])
    
    #food group
    self.collect = pygame.sprite.Group()
    self.collect.add(self.friedrice)
    self.collect.add(self.pizza)
    #self.collect.add(self.lassi)
    self.collect.add(self.cookie)
    
    self.kana = Kana()
  
  def render_main(self):
      self.screen.fill((0,0,0))
      self.screen.blit(self.background, (0,0)) #Draws one surface on top of another surface
        
  def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
  
  #Mathods for each collison that Kana makes with a food object
  def check_collisions_friedrice(self):
    if pygame.sprite.spritecollide(self.kana, self.friedrice, True):
      self.show_friedrice = False
      print(len(self.collect))
      
  

      
  def mainloop(self):
    #select state loop
    run = True
    while run:
      # Blit everything to the screen
      if self.show_textbox == True:
        self.screen.blit(self.box, (0, 0))
        pygame.display.flip()
        
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          print("quit")
          self.quit()
          
        if event.type == pygame.KEYDOWN: #Checks that whether a key is pressed.
          if event.key == pygame.K_SPACE: # renders new area if spacebar is pressed
            self.show_player = True 
            self.show_textbox = False #stops displaying the texbox
            self.show_friedrice = True
            self.show_pizza = True
            self.show_cookie = True
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
      self.render_main() 
      if self.show_player == True:  
        self.screen.blit(self.kana.img, self.kana.rect)
        self.check_collisions_friedrice()
      
      if self.show_friedrice == True:
        self.screen.blit(self.friedrice.img, self.friedrice.rect)
    
      if self.show_pizza == True:
        self.screen.blit(self.pizza.img, self.pizza.rect)
        
      if self.show_cookie == True:
        self.screen.blit(self.cookie.img, self.cookie.rect)
    
        
    
        
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