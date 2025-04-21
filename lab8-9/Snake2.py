import pygame, sys, random, time

pygame.init()


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20


DARK_GRASS = (85, 107, 47)
SNAKE_ORANGE = (255, 140, 0)
TEXT_WHITE = (255, 255, 255)
FOOD_COLORS = {
    1: (180, 0, 0),   
    2: (255, 165, 0), 
    3: (255, 215, 0)  
}

# Шрифт и экран
font = pygame.font.SysFont("Verdana", 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Timed Food & Weights")

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0].copy()
        if self.direction == "RIGHT":
            head[0] += CELL_SIZE
        elif self.direction == "LEFT":
            head[0] -= CELL_SIZE
        elif self.direction == "UP":
            head[1] -= CELL_SIZE
        elif self.direction == "DOWN":
            head[1] += CELL_SIZE
        self.body = [head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, SNAKE_ORANGE, (*block, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        if head in self.body[1:]:
            return True
        return False

# Класс еды с весом и таймером
class Food:
    def __init__(self, snake_body):
        self.spawn_time = time.time()
        self.weight = random.choice([1, 2, 3]) 
        self.color = FOOD_COLORS[self.weight]
        self.position = self.generate(snake_body)

    def generate(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            if [x, y] not in snake_body:
                return [x, y]

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

    def expired(self, timeout=5):
        return time.time() - self.spawn_time > timeout

# Игровая функция
def game():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake.body)

    score = 0
    level = 1
    speed = 10

    running = True
    while running:
        screen.fill(DARK_GRASS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != "DOWN":
            snake.direction = "UP"
        elif keys[pygame.K_DOWN] and snake.direction != "UP":
            snake.direction = "DOWN"
        elif keys[pygame.K_LEFT] and snake.direction != "RIGHT":
            snake.direction = "LEFT"
        elif keys[pygame.K_RIGHT] and snake.direction != "LEFT":
            snake.direction = "RIGHT"

        snake.move()

        # Проверка съедания еды
        if snake.body[0] == food.position:
            score += food.weight
            snake.grow()
            food = Food(snake.body)
            if score % 6 == 0:
                level += 1
                speed += 2

        # Если еда исчезла по таймеру, создаём новую
        if food.expired():
            food = Food(snake.body)

        # Столкновение с собой или стенами
        if snake.check_collision():
            running = False

        # Отрисовка
        snake.draw()
        food.draw()

        # Отображение счёта и уровня
        score_text = font.render(f"Score: {score}", True, TEXT_WHITE)
        level_text = font.render(f"Level: {level}", True, TEXT_WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (WIDTH - 120, 10))

        pygame.display.flip()
        clock.tick(speed)

# Запуск игры
game()
