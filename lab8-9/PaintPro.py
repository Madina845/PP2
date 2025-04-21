import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((0, 0, 0))  
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'       # цвет
    tool = 'pen'        # инструмент по умолчанию
    points = []

    drawing = False
    shape_start = (0, 0)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Цвет
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # Инструменты
                elif event.key == pygame.K_1:
                    tool = 'rect'
                elif event.key == pygame.K_2:
                    tool = 'circle'
                elif event.key == pygame.K_3:
                    tool = 'square'
                elif event.key == pygame.K_4:
                    tool = 'right_triangle'
                elif event.key == pygame.K_5:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_6:
                    tool = 'rhombus'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'pen'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    shape_start = event.pos
                    if tool == 'pen' or tool == 'eraser':
                        points = [event.pos]
                elif event.button == 3:
                    radius = max(1, radius - 1)
                elif event.button == 4:
                    radius = min(200, radius + 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    shape_end = event.pos
                    draw_shape(screen, tool, shape_start, shape_end, radius, 'black' if tool == 'eraser' else mode)

            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == 'pen' or tool == 'eraser':
                    position = event.pos
                    points.append(position)
                    if len(points) >= 2:
                        color_mode = 'black' if tool == 'eraser' else mode
                        drawLineBetween(screen, len(points)-2, points[-2], points[-1], radius, color_mode)

        pygame.display.flip()
        clock.tick(60)

# Функция для рисования фигур
def draw_shape(screen, tool, start, end, width, color_mode):
    color = get_color(color_mode)
    x1, y1 = start
    x2, y2 = end

    if tool == 'rect':
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(screen, color, rect, width)

    elif tool == 'circle':
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
        pygame.draw.circle(screen, color, center, radius, width)

    elif tool == 'square':
        side = min(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, side, side)
        pygame.draw.rect(screen, color, rect, width)

    elif tool == 'right_triangle':
        points = [start, (x1, y2), (x2, y2)]
        pygame.draw.polygon(screen, color, points, width)

    elif tool == 'equilateral_triangle':
        # Центр нижней стороны + вершина сверху
        side = abs(x2 - x1)
        height = int((3 ** 0.5 / 2) * side)
        points = [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)]
        pygame.draw.polygon(screen, color, points, width)

    elif tool == 'rhombus':
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
        pygame.draw.polygon(screen, color, points, width)

def get_color(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'white':
        return (255, 255, 255)
    elif mode == 'black':
        return (0, 0, 0)
    return (255, 255, 255)

# Функция рисования линии (для кисти и ластика)
def drawLineBetween(screen, index, start, end, width, color_mode):
    color = get_color(color_mode)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(screen, color, (x, y), width)

main()
