import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

face=pygame.Rect(100,200,200,200)
eye1=pygame.Rect(120,240,60,30)
eye2=pygame.Rect(220,240,60,30)
mouth=pygame.Rect(165,320,70,30)
while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.draw.rect(screen,(120,120,120),face)      
    pygame.draw.rect(screen,(225,225,0),eye1)        
    pygame.draw.rect(screen,(225,225,0),eye2)        
    pygame.draw.rect(screen,(225,150,150),mouth)      
    
    pygame.display.update()
    clock.tick(30)



