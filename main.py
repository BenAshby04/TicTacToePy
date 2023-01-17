import pygame
from sys import exit

def resetGrid():
    grid = []
    for i in range(9):
        grid.append("-")
    return grid


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

grid = resetGrid()

WHITE = (255,255,255)
GREY = (80,80,80)
BLACK = (0,0,0)

turn = "X"

greyboxes = [pygame.Rect(50,75,100,80),pygame.Rect(200,75,100,80),pygame.Rect(350,75,100,80),
                 pygame.Rect(50,200,100,80),pygame.Rect(200,200,100,80),pygame.Rect(350,200,100,80),
                 pygame.Rect(50,320,100,80),pygame.Rect(200,320,100,80),pygame.Rect(350,320,100,80)]
while gameloop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = resetGrid()
                turn = "X"
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(greyboxes)):
                if greyboxes[i].collidepoint(pygame.mouse.get_pos()):
                    print(i)
                    if turn == "X":
                        if grid[i] == "-":
                            grid[i] = "X"
                            turn = "O"  
                    else:
                        if grid[i] == "-":
                            grid[i] = "O"
                            turn = "X"
    
    screen.fill(BLACK)
    turnFont = pygame.font.Font('freesansbold.ttf',60)
    turnRect = turnFont.render("Turn: " + turn, True, WHITE)
    screen.blit(turnRect, (10,10))

    
    #Grey squares
    #123
    #456
    #789
    
    pygame.draw.rect(screen,GREY,greyboxes[0]) #1
    pygame.draw.rect(screen,GREY,greyboxes[1]) #2
    pygame.draw.rect(screen,GREY,greyboxes[2]) #3
    pygame.draw.rect(screen,GREY,greyboxes[3]) #4
    pygame.draw.rect(screen,GREY,greyboxes[4]) #5
    pygame.draw.rect(screen,GREY,greyboxes[5]) #6
    pygame.draw.rect(screen,GREY,greyboxes[6]) #7
    pygame.draw.rect(screen,GREY,greyboxes[7]) #8
    pygame.draw.rect(screen,GREY,greyboxes[8]) #9
    
    #Draw text for turns
    for i in range(len(greyboxes)):
        if grid[i] != "-":
            
            font = pygame.font.Font('freesansbold.ttf',60)
            textrect = font.render(grid[i],True,WHITE)
            # text = textrect.get_rect()
            # pygame.draw.rect(screen,WHITE,font)
            screen.blit(textrect, (greyboxes[i].x+30, greyboxes[i].y+15))
    #Lines for grid
    pygame.draw.line(screen, WHITE, (167,65), (167,400),4) #Left verticle
    pygame.draw.line(screen,WHITE, (333, 65), (333,400),4) #Right verticle
    pygame.draw.line(screen,WHITE,(40,180),(460,180),4) #Top Horizontal
    pygame.draw.line(screen,WHITE,(40,300), (460,300),4) #Bottom Horizontal
    pygame.display.flip()
    
    clock.tick(60)