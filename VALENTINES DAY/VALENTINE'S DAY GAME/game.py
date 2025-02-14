import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
BASKET_WIDTH, BASKET_HEIGHT = 80, 80
BASKET_Y = HEIGHT - 80  
BASKET_SPEED = 15  # Increased basket speed
HEART_SIZE = 60  
WHITE, RED, PINK = (255, 255, 255), (255, 0, 0), (255, 182, 193)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catching Your LOVE 💖")

# Load Images
try:
    basket_img = pygame.image.load("assets/basket.png")
    basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))
except FileNotFoundError:
    print("Error: 'basket.png' not found in the 'assets' folder.")
    pygame.quit()
    exit()

try:
    heart_img = pygame.image.load("assets/heart.png")
    heart_img = pygame.transform.scale(heart_img, (HEART_SIZE, HEART_SIZE))
except FileNotFoundError:
    print("Error: 'heart.png' not found in the 'assets' folder.")
    pygame.quit()
    exit()

# Basket Position
basket = pygame.Rect(WIDTH // 2 - BASKET_WIDTH // 2, BASKET_Y, BASKET_WIDTH, BASKET_HEIGHT)

# List to Track Hearts
hearts = []
score = 0
high_score = 0
font = pygame.font.Font(None, 36)
message_font = pygame.font.Font(None, 50)

# Game Loop
running = True
game_over = False
clock = pygame.time.Clock()
message_shown = False
message_y = HEIGHT // 2  # Initial Y position of message for floating effect
message_direction = 1  # Controls floating movement

def draw_valentine_message():
    """Draw the floating 'HAPPY VALENTINE DAY' message."""
    global message_y, message_direction
    message_y += message_direction
    if message_y > HEIGHT // 2 + 10 or message_y < HEIGHT // 2 - 10:
        message_direction *= -1  # Reverse direction to float up and down

    message_text = message_font.render("HAPPY VALENTINE DAY", True, RED)
    text_rect = message_text.get_rect(center=(WIDTH // 2, message_y))
    screen.blit(message_text, text_rect)

def ask_to_retry():
    """Ask the player if they want to retry."""
    retry_text = font.render("Press SPACE to Retry or Q to Quit", True, (0, 0, 0))
    screen.blit(retry_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))

while running:
    screen.fill(PINK)  # Background Color

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Move Basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.x > 0:
            basket.x -= BASKET_SPEED
        if keys[pygame.K_RIGHT] and basket.x < WIDTH - BASKET_WIDTH:
            basket.x += BASKET_SPEED

        # Spawn Hearts at Random Intervals
        if random.randint(1, 20) == 1:
            hearts.append([random.randint(0, WIDTH - HEART_SIZE), 0, random.randint(2, 4)])  # Slower falling speed
            # Each heart has (x, y, speed)

        # Move Hearts and Check Collision
        hearts_to_remove = []
        for heart in hearts:
            heart[1] += heart[2]  # Move heart down at its own speed

            # Collision check: If the heart is inside the basket
            if heart[1] + HEART_SIZE > BASKET_Y and basket.x < heart[0] < basket.x + BASKET_WIDTH:
                score += 1  # Increment score
                hearts_to_remove.append(heart)  
            
            elif heart[1] > HEIGHT:                        
                hearts_to_remove.append(heart)
                game_over = True  # Game over if a heart is missed

        # Remove caught or missed hearts
        for heart in hearts_to_remove:
            hearts.remove(heart)

        # Draw Hearts First (Behind Basket)
        for heart in hearts:
            screen.blit(heart_img, (heart[0], heart[1]))  

        # Draw Basket Last (Top)
        screen.blit(basket_img, (basket.x, basket.y))  

        # Score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Update High Score
        if score > high_score:
            high_score = score

        # Check if High Score Reached
        if high_score >= 100:
            game_over = True

    # Game Over Screen
    if game_over:
        # Clear the screen
        screen.fill(PINK)

        # Display High Score
        high_score_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
        screen.blit(high_score_text, (WIDTH // 2 - 70, HEIGHT // 2 - 50))

        # Draw Valentine Message
        draw_valentine_message()

        # Ask to Retry
        ask_to_retry()

        # Check for Retry or Quit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_over = False
            score = 0
            hearts = []
            basket.x = WIDTH // 2 - BASKET_WIDTH // 2  # Reset basket position
        elif keys[pygame.K_q]:
            running = False

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()