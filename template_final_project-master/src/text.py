import pygame

class Text():
    def __init__(self, x, y, text=""):
        """
        makes textboxes
        args: self, 
        
        """
        self.box = pygame.Surface((x - 300, y - 100 ))
        self.box = self.box.convert()
        self.box.fill((250, 250, 250)) # these are colors, size is determined by self.texbox
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(text)
        textpos = self.text.get_rect()
        textpos.centerx = self.box.get_rect().centerx
        self.box.blit(self.text, textpos)