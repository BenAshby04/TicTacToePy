import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode((500,500))
gameloop = True

WHITE = (255,255,255)

while gameloop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit() 
    
    #Lines for grid
    
    pygame.draw.line(screen, WHITE, (167,85), (167,400),4) #Left verticle
    pygame.draw.line(screen,WHITE, (333, 85), (333,400),4) #Right verticle
    pygame.draw.line(screen,WHITE,(50,180),(450,180),4) #Top Horizontal
    pygame.draw.line(screen,WHITE,(50,300), (450,300),4)
    pygame.display.flip()
    clock.tick(60)