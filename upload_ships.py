import pygame

from main import *
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fight")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))

YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))

RED_SPACESHIP_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK, BORDER )
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()
