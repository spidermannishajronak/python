import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CATCH THE STARS.")

clock = pygame.time.Clock()

BACKGROUND = (30,30,50)
BLUE = (50,150,255)

player_width = 100
player_height = 30

player_speed = 7


player_x = WIDTH // 2 - player_width // 2


GAME_PLAYING = "playing"
GAME_OVER = "game_over"

game_state = GAME_PLAYING

running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
     
            
    if game_state == GAME_PLAYING:
        keys = pygame.key.get_pressed()
    
        
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            
        if keys[pygame.K_LEFT]: 
            player_x += player_speed
            
        if player_x < 0:
           player_x = 0 
           
        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width 
            
        
        player_rect = pygame.Rect(player_x, HEIGHT - 60 , player_width , player_height)
        
        pygame.draw.rect(screen, BLUE, player_rect)
        
        
        screen.fill(BACKGROUND)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
sys.exit()