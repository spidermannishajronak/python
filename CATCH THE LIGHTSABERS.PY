import pygame
import random
import os
import sys

pygame.init()

# WINDOW
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lightsaber Catcher")

clock = pygame.time.Clock()

# COLORS
BLACK = (10, 10, 20)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
GREEN = (0, 255, 80)
PURPLE = (180, 0, 255)
RED = (255, 30, 30)

# FONTS
font = pygame.font.SysFont("Arial", 30, bold=True)
big_font = pygame.font.SysFont("Arial", 65, bold=True)

# HIGH SCORE
FILE = "highscore.txt"

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        highscore = int(f.read() or 0)
else:
    highscore = 0

# PLAYER
player = pygame.Rect(350, 530, 100, 25)
PLAYER_SPEED = 7

# LIGHTSABERS
sabers = []
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 850)

# GAME VARIABLES
score = 0
lives = 3
game_over = False

def reset_game():
    global score, lives, game_over, sabers, player

    score = 0
    lives = 3
    game_over = False
    sabers = []
    player.x = 350

def save_highscore():
    global highscore

    if score > highscore:
        highscore = score

        with open(FILE, "w") as f:
            f.write(str(highscore))

def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

def create_saber():
    colors = [
        (BLUE, 5),
        (GREEN, 3),
        (PURPLE, 2),
        (RED, 0)
    ]

    color, points = random.choice(colors)

    saber = {
        "rect": pygame.Rect(
            random.randint(20, WIDTH - 35),
            -60,
            18,
            60
        ),
        "color": color,
        "points": points,
        "speed": random.randint(3, 6)
    }

    sabers.append(saber)

def draw_saber(saber):
    rect = saber["rect"]
    color = saber["color"]

    # Glowing blade
    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=8
    )

    # Handle
    pygame.draw.rect(
        screen,
        (180, 180, 190),
        (rect.x, rect.bottom - 12, rect.width, 12),
        border_radius=3
    )

def draw_player():
    pygame.draw.rect(
        screen,
        (220, 220, 230),
        player,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        BLUE,
        (player.x + 10, player.y + 5, 80, 5),
        border_radius=5
    )

running = True

while running:

    clock.tick(60)
    screen.fill(BLACK)

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_EVENT and not game_over:
            create_saber()

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:

            mouse = pygame.mouse.get_pos()

            play_button = pygame.Rect(210, 370, 170, 60)
            quit_button = pygame.Rect(420, 370, 170, 60)

            if play_button.collidepoint(mouse):
                reset_game()

            elif quit_button.collidepoint(mouse):
                running = False

        if event.type == pygame.KEYDOWN and game_over:

            if event.key == pygame.K_r:
                reset_game()

            elif event.key == pygame.K_q:
                running = False

    # GAME
    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_SPEED

        # Keep player inside screen
        player.x = max(0, min(WIDTH - player.width, player.x))

        # Move lightsabers
        for saber in sabers[:]:

            saber["rect"].y += saber["speed"]

            # Collision
            if player.colliderect(saber["rect"]):

                if saber["color"] == RED:
                    lives -= 1

                else:
                    score += saber["points"]

                    if score > highscore:
                        save_highscore()

                sabers.remove(saber)

            # Saber missed
            elif saber["rect"].top > HEIGHT:
                sabers.remove(saber)

        # Game over
        if lives <= 0:
            game_over = True
            save_highscore()

        # DRAW SABERS
        for saber in sabers:
            draw_saber(saber)

        draw_player()

        # SCOREBOARD
        draw_text(f"Score: {score}", font, WHITE, 20, 20)
        draw_text(f"High Score: {highscore}", font, WHITE, 20, 60)
        draw_text(f"Lives: {lives}", font, WHITE, 650, 20)

    else:

        # GAME OVER SCREEN
        draw_text("GAME OVER!", big_font, RED, 190, 190)

        draw_text(
            f"Your Score: {score}",
            font,
            WHITE,
            300,
            280
        )

        draw_text(
            f"High Score: {highscore}",
            font,
            WHITE,
            290,
            320
        )

        # PLAY AGAIN BUTTON
        pygame.draw.rect(
            screen,
            GREEN,
            (210, 370, 170, 60),
            border_radius=10
        )

        draw_text("PLAY AGAIN", font, BLACK, 220, 385)

        # QUIT BUTTON
        pygame.draw.rect(
            screen,
            RED,
            (420, 370, 170, 60),
            border_radius=10
        )

        draw_text("QUIT", font, WHITE, 465, 385)

        draw_text(
            "Press R to restart or Q to quit",
            font,
            WHITE,
            190,
            470
        )

    pygame.display.update()

pygame.quit()
sys.exit()
