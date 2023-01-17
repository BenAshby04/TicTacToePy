import pygame
from sys import exit

#Classes
class greyblock:
    def __init__(self, x,y,color):
        self.x =x
        self.y =y
        self.color = color


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode((500,500))
gameloop = True

WHITE = (255,255,255)
GREY = (80,80,80)

while gameloop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit() 
    
    
    #Grey squares
    #123
    #456
    #789
    
    pygame.draw.rect(screen,GREY,pygame.Rect(50,75,100,80)) #1
    pygame.draw.rect(screen,GREY,pygame.Rect(200,75,100,80)) #2
    pygame.draw.rect(screen,GREY,pygame.Rect(350,75,100,80)) #3
    pygame.draw.rect(screen,GREY,pygame.Rect(50,200,100,80)) #4
    pygame.draw.rect(screen,GREY,pygame.Rect(200,200,100,80)) #5
    pygame.draw.rect(screen,GREY,pygame.Rect(350,200,100,80)) #6
    pygame.draw.rect(screen,GREY,pygame.Rect(50,320,100,80)) #7
    pygame.draw.rect(screen,GREY,pygame.Rect(200,320,100,80)) #8
    pygame.draw.rect(screen,GREY,pygame.Rect(350,320,100,80)) #9
    
    #Lines for grid
    pygame.draw.line(screen, WHITE, (167,65), (167,400),4) #Left verticle
    pygame.draw.line(screen,WHITE, (333, 65), (333,400),4) #Right verticle
    pygame.draw.line(screen,WHITE,(40,180),(460,180),4) #Top Horizontal
    pygame.draw.line(screen,WHITE,(40,300), (460,300),4) #Bottom Horizontal
    pygame.display.flip()
    
    clock.tick(60)