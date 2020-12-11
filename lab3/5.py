import pygame
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((600, 400))
BLACK = (0, 0, 0)
YELLOW = (255, 247, 29)
SKY = (161, 245, 255)
SEA = (68, 35, 223)
TOMATO = (244, 81, 81)
BROWN = (199, 47, 10)
GREY = (222, 213, 153)
WHITE = (255, 255, 255)

screen.fill(SKY)
rect(screen, SEA, (0, 185, 600, 215))
rect(screen, YELLOW, (0, 280, 600, 215))

circle(screen, YELLOW, (535, 55), 35)

circle(screen, WHITE, (132, 40), 15)
circle(screen, GREY, (132, 40), 15, 1)
circle(screen, WHITE, (145, 40), 15)
circle(screen, GREY, (145, 40), 15, 1)
circle(screen, WHITE, (165, 45), 15)
circle(screen, GREY, (165, 45), 15, 1)
circle(screen, WHITE, (120, 55), 15)
circle(screen, GREY, (120, 55), 15, 1)
circle(screen, WHITE, (140, 53), 15)
circle(screen, GREY, (140, 53), 15, 1)
circle(screen, WHITE, (160, 55), 15)
circle(screen, GREY, (160, 55), 15, 1)
circle(screen, WHITE, (175, 55), 15)
circle(screen, GREY, (175, 55), 15, 1)

rect(screen, BROWN, (95, 230, 5, 150))
polygon(screen, TOMATO, [(25, 260), (97, 228),
                        (170, 260), (25, 260)])
x = 25
h = (170-25)//8
for i in range(9):
    line(screen, BLACK, (97, 228), (x, 260))
    x += h

circle(screen, BROWN, (350, 200), 25,
       draw_bottom_left=True)
rect(screen, BROWN, (350, 200, 150, 25))
polygon(screen, BROWN, [(500, 200), (560, 200),
                        (500, 225), (500, 200)])
circle(screen, WHITE, (510, 210), 7)
circle(screen, BLACK, (510, 210), 9, 3)
rect(screen, BLACK, (400, 100, 5, 100))
polygon(screen, GREY, [(405, 200), (475, 150),
                       (425, 150), (405, 200)])
polygon(screen, BLACK, [(405, 200), (475, 150),
                       (425, 150), (405, 200)], 1)
polygon(screen, GREY, [(405, 100), (475, 150),
                       (425, 150), (405, 100)])
polygon(screen, BLACK, [(405, 100), (475, 150),
                       (425, 150), (405, 100)], 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
