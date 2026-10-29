import pygame
import sys
import random
import os

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CATCH THE STARS.")

clock = pygame.time.Clock()

BACKGROUND = (30,30,50)
BLUE = (50,150,255)
YELLOW = (225,220,50)
WHITE = (255,255,255)
RED = (255,80,80)
GREEN = (80,220,120)

font = pygame.font.Font(None, 40)
medium_font = pygame.font.Font(None, 55)
big_font = pygame.font.Font(None, 80)

player_width = 100
player_height = 30

player_speed = 7

star_size = 30
star_speed = 4
MAX_LIVES = 3

HIGH_SCORE_FILE = "caththestar.txt"

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except ValueError:
            return 0
    return 0 

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))
             
high_score = load_high_score()  


      
def reset_game():
    player_x = WIDTH // 2 - player_width // 2
    star_x = random.randint( 0, WIDTH - star_size)
    star_y = -star_size
    score = 0
    lives = MAX_LIVES
    speed = 5
     
    return ( player_x,star_x,star_y,score,lives,speed)

( player_x,star_x,star_y,score,lives,speed) = reset_game()


GAME_PLAYING = "playing"
GAME_OVER = "game_over"

game_state = GAME_PLAYING

running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                (
                   player_x,
                   star_x,
                   star_y,
                   score,
                   lives, 
                   star_speed     
                ) = reset_game()
            
    if game_state == GAME_PLAYING:
        keys = pygame.key.get_pressed()
        screen.fill(BACKGROUND)
        
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            
        if keys[pygame.K_RIGHT]: 
            player_x += player_speed
            
        if player_x < 0:
           player_x = 0 
           
        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width 
            
        star_y += star_speed
        
        
        player_rect = pygame.Rect(player_x, HEIGHT - 60 , player_width , player_height)
        star_rect = pygame.Rect( star_x, star_y, star_size, star_size )
        
        pygame.draw.rect(screen, BLUE, player_rect)
        pygame.draw.circle(screen , YELLOW, star_rect.center, star_size // 2)
        
        
        if player_rect.colliderect(star_rect):
            score += random.randint(10,20)
            star_x = random.randint ( 0, WIDTH - star_size)
            star_y = -star_size
            star_speed += 0.01
        if star_y >  HEIGHT:
            lives -= 1
            star_x = random.randint(0, WIDTH - star_size)
            star_y = -star_size
                    
            if lives <=0:
                        game_state = GAME_OVER
                        if score > high_score:
                            high_score = score
                            save_high_score(high_score)
                       
        
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit( score_text, (20,20) )
            
            high_score_text = font.render(f"High Score:{high_score} " , True,WHITE)
            screen.bilt(high_score_text , (20,60))
            
            lives_text = font.render(f"Lives: {lives}", True, WHITE)
            screen.blit( lives_text, (WIDTH - 150,20) )
            
    elif game_state == GAME_OVER:
        screen.fill(BACKGROUND)
        game_over_text = big_font.render(f"GAME OVER", True,RED)
        screen.bilt( game_over_text, ( WIDTH // 2 - game_over_text.get.width() // 2,120))
        
        final_score_text = medium_font.render(f"Score: {score}", True, WHITE)
        screen.bilt( final_score_text, ( WIDTH // 2 - final_score_text.get_width() // 2, 230))
        
        high_score_text = font.render(f"High_Score: {high_score}", True, YELLOW)
        screen.bilt( high_score_text, ( WIDTH // 2 - high_score_text.get_width() // 2, 230))
        
        restart_text = font.render(f"Press R To Play Again", True, GREEN)
        screen.bilt( restart_text, ( WIDTH // 2 - restart_text.get_width() // 2, 400))
                
        quit_text = font.render(f"Press ESC To Quit", True, RED)
        screen.bilt( quit_text, ( WIDTH // 2 - quit_text.get_width() // 2, 450))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()