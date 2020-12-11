import pygame
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
RED = (255, 0, 0)

screen.fill((200, 0, 200))
circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 100, 1)
circle(screen, RED, (250, 180), 20)
circle(screen, RED, (150, 180), 25)
circle(screen, BLACK, (250, 180), 20, 1)
circle(screen, BLACK, (150, 180), 25, 1)
circle(screen, BLACK, (250, 180), 10)
circle(screen, BLACK, (150, 180), 10)
rect(screen, BLACK, (150, 250, 100, 20))
polygon(screen, BLACK, [[180, 170], [185, 165],
                       [105, 110], [100, 115]])
polygon(screen, BLACK, [[220, 170], [215, 165],
                       [300, 140], [305, 145]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
