import datetime
import sys

import pygame


def load_image(name, size=None):
    image = pygame.image.load(name).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image


pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = load_image("clock.png", (WIDTH, HEIGHT))
minute_hand = load_image("right_hand.png", (140, 140))
second_hand = load_image("left_hand.png", (150, 150))


def rotate_center(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    return rotated_image, new_rect


while True:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Get system time
    now = datetime.datetime.now()
    minutes_angle = -(now.minute * 6)
    seconds_angle = -(now.second * 6)

    # Rotate hands
    min_hand, min_rect = rotate_center(minute_hand, minutes_angle, (300, 300))
    sec_hand, sec_rect = rotate_center(second_hand, seconds_angle, (300, 300))

    # Draw hands
    screen.blit(min_hand, min_rect)
    screen.blit(sec_hand, sec_rect)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
