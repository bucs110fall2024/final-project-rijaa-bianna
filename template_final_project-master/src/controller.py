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
    '''^^This makes the inital screen of pygame'''
    
    #variables to control what shows on the screen
    self.count = 0
    self.show_player = False
    self.show_textbox = True # start game controls the textbox display
    self.show_friedrice = False
    self.show_pizza = False
    self.show_cookie = False
    self.show_lassi = False
    self.tomo_pet = False
    '''^^ These are the variables that control what shows on the screen'''
    
    #Put food here
    self.friedrice = Food("template_final_project-master/assets/friedrice.png", self.dimensions[0], self.dimensions[1])
    self.pizza = Food("template_final_project-master/assets/pizza.png", self.dimensions[0], self.dimensions[1])
    self.lassi = Food("template_final_project-master/assets/lassi.png", self.dimensions[0], self.dimensions[1])
    self.cookie = Food("template_final_project-master/assets/cookie.png", self.dimensions[0], self.dimensions[1])
    '''This makes the food objects'''
    
    '''MAKES THE FOOD OBJECTS INTO SPRITES SO THAT THEY HAVE THEY CAN ACCESS THE ABILITIES OF A SPRITE ON PYGAME---'''
    #food group
    self.friedrice_sprite = pygame.sprite.Group()
    self.friedrice_sprite.add(self.friedrice)
    
    self.pizza_sprite = pygame.sprite.Group()
    self.pizza_sprite.add(self.pizza)
    
    self.lassi_sprite = pygame.sprite.Group()
    self.lassi_sprite.add(self.lassi)
    
    self.cookie_sprite = pygame.sprite.Group()
    self.cookie_sprite.add(self.cookie)
    '''-----------------------------------------------------------------------------------------------------------'''
    
    self.kana = Kana() 
    '''^^This makes the Kana sprite exist. Similar to the way turtle works in Turtle()'''
  
  def textbox_message(self):
    if self.count == 0:
      return(f"Hello there, my name is Kana. Help me collect food to feed my cat. Press space to continue")
    if self.count == 4:
      return(f"Yippee! You have collected all the foods. Thank you! Press RETURN KEY to pet Tomo the cat.")
  
  def the_textbox(self):
    #textbox
    self.box = pygame.Surface((self.dimensions[0] - 300, self.dimensions[1] - 100 ))
    self.box = self.box.convert()
    self.box.fill((250, 250, 250)) # these are colors, size is determined by self.texbox
    '''^^Makes the textbox and other varibles of it, such as color and size'''
    
    # Display some text
    self.font = pygame.font.Font(None, 36)
    text = self.font.render(self.textbox_message(), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = self.box.get_rect().centerx
    self.box.blit(text, textpos)
    '''^^Continuation of textbox, determining what it is going to display and blits it on the screen'''
  
  def render_main(self):
      self.screen.fill((0,0,0))
      self.screen.blit(self.background, (0,0)) #Draws one surface on top of another surface
      """
      renders map.jpeg
      arg: self
      return: shows the actual background on screen, map.jpeg
      """
        
  def quit(self): #code to quit the program. Command c on the terminal works too I think
        pygame.quit()
        sys.exit()
        ''' 
        lets the program quit
        arg: self
        return: sys.exit
        '''
  
  '''CHECKS COLLISIONS FOR EACH FOOD SPRITES WITH KANA---------------------'''
  #Methods for each collison that Kana makes with a food object
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
      
      '''For all four methods above:
      Checks for collisions with food sprites with Kana Sprite.
      If the two sprites collides, the food object disappears.
      Then, it adds a count to the amount of Kana and food collisions made.
      arg: self
      return: sprite visiblity and kana-and-food-sprite collision counter goes up by one'''
  '''----------------------------------------------------------------------------------'''
  
  def tomo_interact(self):
    self.tomo_petted = pygame.image.load("template_final_project-master/assets/characters/tomoopen-removebg-preview.png")
    self.tomo_rect2 = self.tomo_petted.get_rect()
    self.screen.blit(self.tomo_petted, self.tomo_rect2)
    '''
    Triggers an interaction with Tomo, our pet, which shows up at the end of the game. 
    arg: self
    returns: overlaps a image of Tomo with their mouth open to show a "petting animation"
    '''
  
  def mainloop(self):
    #select state loop
    run = True
    while run:
        
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
            '''^^ Kana, our player's avatar, is reblited 50 pixels down (Determined by self.speed in Kana.py)'''
          if event.key == pygame.K_UP:
            self.kana.move_up()
            '''^^ ^^ Kana, our player's avatar, is reblited 50 pixels up (Determined by self.speed in Kana.py)'''
          if event.key == pygame.K_LEFT:
            self.kana.move_left()
            '''^^ Kana, our player's avatar, is reblited 50 pixels left (Determined by self.speed in Kana.py)'''
          if event.key == pygame.K_RIGHT:
            self.kana.move_right()
            '''^^ Kana, our player's avatar, is reblited 50 pixels right (Determined by self.speed in Kana.py)'''
          """------------------------------------------------------------------"""
          
          if event.key == pygame.K_RETURN:
            self.tomo_pet = True
            '''Triggers the tomo_pet if statment which triggers the tomo_interact method allowing a petting animation. 
            This is for the end of the game.'''
          
      self.render_main() 
      '''^^Re-blits the map so that the old image of Kana, the player, doesn't show and only the most recent shows.
      Gives the illusion that Kana, our player, is moving'''
      
      if self.show_player == True:
        self.screen.blit(self.kana.img, self.kana.rect)
        self.check_collisions_friedrice()
        self.check_collisions_pizza()
        self.check_collisions_lassi()
        self.check_collisions_cookie()
      ''' ^^ When show_player is True, it makes our player show on the screen.
      And so, when the player moves around the screen, program constantly checks for collision
      between Kana sprite and food sprites'''
      
      '''CONTROLS THE VISIBILITY OF THE FOOD, IF THE if statement IS TRUE, THEN SHOW BLITS THE FOOD. IF FALSE THEN IT NO LONGER SHOWS'''
      if self.show_friedrice == True:
        self.screen.blit(self.friedrice.img, self.friedrice.rect)
    
      if self.show_pizza == True:
        self.screen.blit(self.pizza.img, self.pizza.rect)
      
      if self.show_lassi == True:
        self.screen.blit(self.lassi.img, self.lassi.rect)
        
      if self.show_cookie == True:
        self.screen.blit(self.cookie.img, self.cookie.rect)
      '''--------------------------------------------------------------------------------------------------------------------------------'''
      
      if self.count == 4:
        self.show_textbox = True
      '''^^When self.count == 4, as in when the player has collided with all 4 foods on the screen, run the textbox code 
      for another texbox to pop up'''
      
      '''TO CONTROL THE TEXTBOX AND THINGS THAT HAPPEN WHEN THE TEXTBOX IS UP ON SCREEN ------------------------------------'''
      if self.show_textbox == True:
        self.the_textbox()
        self.screen.blit(self.box, (0, 0))
        
        if self.count == 4: #Checking to see if the game has ended
          self.tomo = pygame.image.load("template_final_project-master/assets/characters/tomo.png")
          self.tomo_rect = self.tomo.get_rect()
          self.screen.blit(self.tomo, self.tomo_rect)
          '''^^^When game has ended, (when self.count == 4),tomo pops up onto the screen'''
          if self.tomo_pet == True:
            self.tomo_interact()
            pygame.time.delay(1000)
            '''Let's you interact with Tomo, through triggering self.tomo_interact'''
            
          self.kanaimg = pygame.image.load("template_final_project-master/assets/characters/kanaopen-removebg-preview.png")
          self.kana_rect = self.kanaimg.get_rect()
          self.screen.blit(self.kanaimg, (300, self.kana_rect[1]))
        '''To explain: There are two stages of our textbox. Once for the beginning of the game (when self.count = 0),
        second, for the end (when self.count = 4). Note: self.count is the number of times kana, our player, and the food sprites have collided
        Therefore, beginning of game and end of game is determined by this count.'''
        '''--------------------------------------------------------------------------------------------------------------'''
        
          
        
      pygame.display.flip() 
      '''^^^Displays the surface onto the screen at the very end of the loop'''