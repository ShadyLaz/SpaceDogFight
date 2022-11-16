import pygame.draw

from ship_movement import *
from upload_ships import *



def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
