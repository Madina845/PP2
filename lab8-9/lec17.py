import pygame
import random

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width,height))

#variables and their initialization
score = 0
fruit_eaten = False

fr_x = random.randrange(1,width//10)*10
fr_y = random.randrange(1,height//10)*10
fruit_coor = [fr_x,fr_y]

head_square = [100,100]

squares =[
    [30,100],
    [40,100],
    [50,100],
    [60,100],
    [70,100],
    [80,100],
    [90,100],
]

direction = "right"
next_dir = "right"

done = False
d
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(255,0,0),pygame.Rect)

    pygame.display.flip()

pygame.quit()
        #todo
squares.appen

print(squares)

#drawing section
screen.fill((0,0,0))

fruit