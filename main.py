#main.py
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Create player
    
    
    #Create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    #Create player (NB. Must be created after groups)
    player = Player(x, y, 20)

    #Create AsteroidField
    asteroid_field = AsteroidField()
    
    #Create game loop
    running = True
    #Check if app needs to quit
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update updatables
        for obj in updateable:
            obj.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("GAME OVER!")
                running = False
        #Render the screen at 60FPS
        screen.fill(color=(0, 8, 8))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()
   
