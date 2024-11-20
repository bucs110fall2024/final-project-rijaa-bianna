
class Controller:
  
  def __init__(self):
    #setup pygame data
<<<<<<< HEAD
  
=======
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    self.kana = Kana()
    self.inventory =[]
    self.npc = []
    
    
>>>>>>> 67c4b1ffd930074e27bf41e6df46610b78aef095
  def mainloop(self):
    #select state loop
    for event in pygame.events.get():
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
