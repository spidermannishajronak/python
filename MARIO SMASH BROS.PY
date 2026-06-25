import pygame
import random
import sys

pygame.init()

W, H = 500,600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("MARIO")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 60)

player = pygame.Rect(220, 540, 60, 30)

coins = []
bombs = []

score = 0
lives = 10
game_over = False

def load_high_score():
    try:
        with open("coinscore.txt" , "r") as file:
            return int(file.read())
    except:
        with open("coinscore.txt" , "w") as file:
            file.write("0")
        return 0
high_score = load_high_score()
        
def save_high_score(high_score):
    with open("coinscore.txt" , "w")as file:
            file.write(str(high_score))
            


def reset_game():
    global score, lives, coins, bombs, game_over
    score = 0
    lives = 10
    coins = []
    bombs = []
    player.x = 220
    game_over = False

while True:
    clock.tick(60)
    win.fill((25, 25, 40))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if game_over and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                reset_game()
            if e.key == pygame.K_q:
                pygame.quit()
                sys.exit()
                
    keys = pygame.key.get_pressed()
    
    if not game_over:
        if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= 7
                
        if keys[pygame.K_RIGHT] and player.x < W - player.width:
                player.x += 7
        
        if random.randint(1,25) == 1:
            coins.append(pygame.Rect(random.randint(0, W -25), - 30 , 25 , 25))
            
        if random.randint(1,45) == 1:
            bombs.append(pygame.Rect(random.randint(0, W -30), - 30 , 30 , 30))
            
        for coin in coins[:]:
            coin.y +=5
            if coin.y > H:
                coins.remove(coin)
            elif coin.colliderect(player):
                coins.remove(coin)
                score += random.randint(10 , 20)
            
        for bomb in bombs[:]:
            bomb.y +=6
            if bomb.y > H:
                bombs.remove(bomb)
            elif bomb.colliderect(player):
                bombs.remove(bomb)
                lives -= 1
                if lives == 0:
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)   
                    game_over = True
                
    pygame.draw.rect(win, (80 , 200 , 255) , player)
    
    for coin in coins:
        pygame.draw.ellipse(win, (255 , 220 , 0) , coin)
    
    for bomb in bombs:
         pygame.draw.circle(win, (255 , 70 , 70) , bomb.center , 15)
         
    score_text = font.render(f"Score: {score}" , True,(225,225,225))
    life_text = font.render(f"Lives: {lives}" , True,(225,225,225))
    high_score_text =  font.render(f"High_score: {high_score}" , True,(225,165,0))
    
    win.blit(score_text,(10,10))
    win.blit(life_text,(380,10))
    win.blit(high_score_text,(170,10))
    
    
    if game_over:
        over_text = big_font.render("GAME OVER:" ,True , (255,80,80))
        again_text = font.render("PRESS R TO PLAY AGAIN:" ,True ,(225,225,225))
        quit_text = font.render("PRESS Q TO PLAY QUIT:" ,True ,(225,225,225))
        
        final_score_text = font.render(f"Final score: {score}" , True,(225,165,0))
        best_score_text =  font.render(f"High_score: {high_score}" , True,(0,0,225))
    
    
        win.blit(over_text,(110,120))
        win.blit( again_text,(130,300))
        win.blit(quit_text,(150,340))
        win.blit(final_score_text,(150,390))
        win.blit(best_score_text,(150,430))
    
    pygame.display.update()