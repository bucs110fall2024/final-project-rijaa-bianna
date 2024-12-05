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
    self.count = 0
    self.show_player = False
    self.show_textbox = True # start game controls the textbox display
    self.show_friedrice = False
    self.show_pizza = False
    self.show_cookie = False
    self.show_lassi = False
    
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
    self.lassi = Food("template_final_project-master/assets/lassi.png", self.dimensions[0], self.dimensions[1])
    self.cookie = Food("template_final_project-master/assets/cookie.png", self.dimensions[0], self.dimensions[1])
    
    #food group
    self.friedrice_sprite = pygame.sprite.Group()
    self.friedrice_sprite.add(self.friedrice)
    
    self.pizza_sprite = pygame.sprite.Group()
    self.pizza_sprite.add(self.pizza)
    
    self.lassi_sprite = pygame.sprite.Group()
    self.lassi_sprite.add(self.lassi)
    
    self.cookie_sprite = pygame.sprite.Group()
    self.cookie_sprite.add(self.cookie)
    
    self.kana = Kana()
  
  def render_main(self):
      self.screen.fill((0,0,0))
      self.screen.blit(self.background, (0,0)) #Draws one surface on top of another surface
      """
      ^^^ renders map.jpeg
      """
        
  def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
        ''' 
        ^^ lets the program quit
        '''
  
  #Mathods for each collison that Kana makes with a food object
  def check_collisions_friedrice(self):
    if pygame.sprite.spritecollide(self.kana, self.friedrice_sprite, True):
      self.show_friedrice = False
      self.count += 1
  def check_collisions_pizza(self):
    if pygame.sprite.spritecollide(self.kana, self.pizza_sprite, True):
      self.show_pizza = False
      self.count += 1
  def check_collisions_lassi(self):
    if pygame.sprite.spritecollide(self.kana, self.lassi_sprite, True):
      self.show_lassi = False
      self.count += 1
  def check_collisions_cookie(self):
    if pygame.sprite.spritecollide(self.kana, self.cookie_sprite, True):
      self.show_cookie = False
      self.count += 1
  

      
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
          '''^^ Let's the program quit with clicking the X on the top'''
        if event.type == pygame.KEYDOWN: #Checks that whether a key is pressed.
          if event.key == pygame.K_SPACE: # renders new area if spacebar is pressed
            self.show_player = True 
            self.show_textbox = False #stops displaying the texbox
            self.show_friedrice = True
            self.show_pizza = True
            self.show_lassi = True
            self.show_cookie = True
            '''^^ When Space bar is clicked, the game starts. The displays our player, Kana.
            Furthermore, it deletes the inital textbox and displays the food items across the screen'''
          
          '''KEY MOVEMENTS FOR KANA, OUR PLAYER---------------------------------'''
          if event.key == pygame.K_DOWN:
            self.kana.move_down()
            '''^^ Let's Kana, our player, move down when down arrow is clicked'''
          if event.key == pygame.K_UP:
            self.kana.move_up()
            '''^^ Let's Kana, our player, move up when up arrow is clicked'''
          if event.key == pygame.K_LEFT:
            self.kana.move_left()
            '''^^ Let's Kana, our player, move left when left arrow is clicked'''
          if event.key == pygame.K_RIGHT:
            self.kana.move_right()
            '''^^ Let's Kana, our player, move right when right arrow is clicked'''
          """------------------------------------------------------------------"""
          
      self.render_main() 
      
      if self.show_player == True:  
        self.screen.blit(self.kana.img, self.kana.rect)
        self.check_collisions_friedrice()
        self.check_collisions_pizza()
        self.check_collisions_lassi()
        self.check_collisions_cookie()
      ''' ^^ When show_player is True, it makes our player show on the screen.
      And so, when the player moves around the screen, program constantly checks for collision
      between Kana sprite and food sprites'''
      if self.show_friedrice == True:
        self.screen.blit(self.friedrice.img, self.friedrice.rect)
    
      if self.show_pizza == True:
        self.screen.blit(self.pizza.img, self.pizza.rect)
      
      if self.show_lassi == True:
        self.screen.blit(self.lassi.img, self.lassi.rect)
        
      if self.show_cookie == True:
        self.screen.blit(self.cookie.img, self.cookie.rect)
      
      if self.count == 4:
        pass
    
        
    
        
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