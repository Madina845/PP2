import pygame
import sys
import datetime


# Load images
def load_image(name, size=None):
    image = pygame.image.load(name).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image


# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load Mickey clock assets
background = load_image("clock.png", (WIDTH, HEIGHT))
minute_hand = load_image("right_hand.png", (200, 50))
second_hand = load_image("left_hand.png", (200, 50))

# Координаты центра вращения (основание рук)
pivot_point = (WIDTH // 2, HEIGHT // 2)


def rotate_hand(image, angle, pivot, hand_offset):
    """
    Вращает изображение вокруг указанной точки (основания руки).
    :param image: поверхность Pygame с изображением руки
    :param angle: угол поворота (в градусах)
    :param pivot: координаты центра вращения
    :param hand_offset: смещение от pivot до центра руки
    :return: повернутая картинка и ее новая позиция
    """
    # Вращаем руку
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect()

    # Корректируем положение руки
    rotated_rect.center = (
        pivot[0] + hand_offset[0] * pygame.math.cos(angle * (3.14 / 180)),
        pivot[1] + hand_offset[1] * pygame.math.sin(angle * (3.14 / 180))
    )

    return rotated_image, rotated_rect


while True:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Получаем время
    now = datetime.datetime.now()
    minutes_angle = -(now.minute * 6)  # 6 градусов за минуту
    seconds_angle = -(now.second * 6)

    # Смещение рук (их основание)
    minute_offset = (100, 0)  # Длина руки
    second_offset = (100, 0)

    # Вращаем руки
    min_hand, min_rect = rotate_hand(minute_hand, minutes_angle, pivot_point, minute_offset)
    sec_hand, sec_rect = rotate_hand(second_hand, seconds_angle, pivot_point, second_offset)

    # Отображаем руки
    screen.blit(min_hand, min_rect)
    screen.blit(sec_hand, sec_rect)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
