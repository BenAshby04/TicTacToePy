import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))
gameloop = True

while gameloop:
    
    for event in pygame.event.get(): 
        if event == pygame.QUIT:
            pygame.quit()
            exit() 
            
pygame.display.flip()
clock.tick(60)