
class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    self.kana = Kana()
    self.inventory =[]
    self.npc = []
    
  def mainloop(self):
    #select state loop
    for event in pygame.events.get():
      pass
  
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
