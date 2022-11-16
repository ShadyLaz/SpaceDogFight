from main import *
import pygame

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:  # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:  # Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:  # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP]:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        red.y += VEL