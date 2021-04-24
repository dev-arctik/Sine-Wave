
import pygame
import math

pygame.init()
win = pygame.display.set_mode((500,500))



run = True
while run:
    

    
    win.fill((0,0,0))
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            run = False

    for x in range(50):
        pygame.time.delay(25)
        x = ((math.pi*x)/180)*700
        y = 75*math.sin(x)+250
        
        pygame.draw.circle(win, (250,250,250), (int(x),int(y)), 5)
       
        
    
        pygame.display.update()


pygame.quit()
