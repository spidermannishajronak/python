import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 640 , 480
CELL_SIZE = 20
COLUMNS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE CLASH")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None , 36)

def draw_rect(pos,color):
    r = pygame.rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(SCREEN, color, r)
  
def random_food(snake):
    while True:
        x = random.randint(0, COLUMNS - 1)  
        y = random.randint(0, ROWS - 1)
        if (x,y) not in snake:
            return (x,y)
        
def show_text(text, size, color, center):
    f = pygame.font.SysFont(None, size)
    s = f.render(text, True, color)
    r = s.get_rect(center=center)
    SCREEN.blit(s, r)
    
def game_loop():
    snake = [(COLUMNS // 2 , ROWS // 2)] 
    direction =  (1, 0)    
    food = random_food(snake)
    score = 0
    speed = 7
    running = True
    paused = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP) and direction != (0, 1):
                direction = (0, -1)
            elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0, -1):
                direction = (0, 1)       
            
            elif event.key in (pygame.k_a, pygame.K_LEFT) and direction != (1, 0):
                direction = (-1, 0)        
                
            elif event.key in (pygame.k_d, pygame.K_UP) and direction != (-1, 0):
                direction = (1, 0)        
            elif event.key == pygame.K_p:  
                paused = not paused
            elif event.key == pygame.K_r and not running:  
                return True
            
            
        if paused:
            SCREEN.FILL((0 , 0 , 0))
            show_text("GAME IS PAUSED.PRESS P TO RESUME" , 36, (255, 255, 255) , (WIDTH // 2 , HEIGHT) // 2)
            pygame.display.flip()
            CLOCK.tick(10)
            continue
        
        head = (snake[0][0] + direction[0] , snake[0][1] + direction[1])
        
        
        
        if head[0] < 0 or head[0] >= COLUMNS or head[1] < 0 or head[1] >= ROWS or head in snake:
            SCREEN.fill((0 , 0 , 0))
            show_text(f"GAME OVER - SCORE: {score}" , 40,(225,0,0),(WIDTH // 2, HEIGHT //2 - 20))
            show_text(f"PRESS R TO RESTART OR Q TO QUIT" , 28,(225,225,225),(WIDTH // 2, HEIGHT //2 + 30))
            pygame.display.flip()
            
        game_over = True
        while game_over:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.k_r:
                        return True
                    if e.key == pygame.k_q:
                        pygame.quit()
                        sys.exit()
                CLOCK.tick(10)    
                
            snake.insert(0, head) 
            
            if head == food:
                score += 1
                
            food = random_food(snake) 
            if score % 5 == 0:
                speed += 1
            else:
                snake.pop()
                
                
                
            SCREEN.fill((0, 0 ,0))
            draw_rect(food,(225, 0, 0))
            for i, segment in enumerate(snake):
                color = (0, 200, 0) if i == 0 else (0, 120, 0)
                draw_rect(segment, color)
                
            show_text(f"Score:{score}" , 28, (255, 255 ,255), (80,20))
            pygame.display.flip()
            CLOCK.tick(speed)
            
if __name__ == "__main__":
    while True:
        restart = game_loop()
        if not restart():
            break