import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((0, 0, 0))  
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'       # цвет
    tool = 'pen'        # инструмент: pen, rect, circle, eraser
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
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'pen'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка — рисовать
                    drawing = True
                    shape_start = event.pos
                    if tool == 'pen' or tool == 'eraser':
                        points = [event.pos]
                elif event.button == 3:  # правая — уменьшить кисть
                    radius = max(1, radius - 1)
                elif event.button == 4:  # колёсико вверх — увеличить
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
