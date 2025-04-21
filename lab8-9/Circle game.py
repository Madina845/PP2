import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Ball properties
ball_radius = 25
rec_x = 10
rec_y = 10
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Start at center
speed = 20  # Movement speed

running = True
while running:
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rectan(screen, (0, 255, 0), (ball_x, ball_y), (rec_x, rec_y))  # Red ball

    pygame.display.flip()
    clock.tick(30)  # Limit FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - speed - ball_radius >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + speed + ball_radius <= HEIGHT:
        ball_y += speed
    if keys[pygame.K_LEFT] and ball_x - speed - ball_radius >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + speed + ball_radius <= WIDTH:
        ball_x += speed

pygame.quit()
