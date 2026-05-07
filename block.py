import pygame
import random
import sys

pygame.init()
W, H = 500 , 600
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("BLOCKY NINJA")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 36)


player = pygame.Rect(225, 540, 40, 40)
blocks = []
speed = 5
score = 0


def reset():
    global blocks, score
    score = 0
    player.x = 225
    
while True:
    clock.tick(60)
    win.fill((20, 20, 30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 6
    if keys[pygame.K_RIGHT] and player.x < W - 50: 
            player.x += 6
            
    for b in blocks:
        b.y += speed
        if b.y > H:
            blocks.remove(b)
            score += 1
        if b.colliderect(player):
            reset()
            
        
    pygame.draw.rect(win, (100, 200, 225) , player)
    for b in blocks:
        pygame.draw.rect(win, (225, 90, 90) , b)  
        
    txt = font.render(f"score:{score}", True , (230,230,230))
    win.blit(txt, (10 , 10))
    pygame.display.update()
    