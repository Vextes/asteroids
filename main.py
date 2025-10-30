# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player setup
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    # asteroids setup
    Asteroid.containers = (asteroids, updatable, drawable)

    # shots setup
    Shot.containers = (shots, updatable, drawable)

    # asteroid field setup
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    #Gameloop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        updatable.update(dt)

        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                print("Game over!")
                running = False

        screen.fill("black")
        
        for drawable_thing in drawable:
            drawable_thing.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
