import pygame
from constants import *
from player import *

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

    player = Player(x,y,20)

    running = True
    #Check if app needs to quit
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update player on the screen
        player.update(dt)
        #Render the screen at 60FPS
        screen.fill(color=(0, 5, 5))
        player.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()
    
