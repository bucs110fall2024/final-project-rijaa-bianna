import pygame
from src.controller import Controller

#import your controller

def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    run = True
    while run: #Pygame automatically exits onces its done with the program. This keep pygame running
        for event in pygame.event.get():
            pass
    mycontroller = Controller()
    
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
