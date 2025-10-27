# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.set_mode(size)
    while():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill((255,255,255))
        pygame.display.flip()


if __name__ == "__main__":
    main()
