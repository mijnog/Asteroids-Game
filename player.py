#player.py
import pygame
from circleshape import CircleShape
from constants import *
class Player(CircleShape):

    def __init__(self, x, y, PLAYER_RADIUS):
        # Pass x, y, and PLAYER_RADIUS to the CircleShape constructor
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.x = int(x)
        self.y = int(y)
        self.rotation = 0       
        print(f"Player class initialized at position ({self.x}, {self.y}) with radius {PLAYER_RADIUS}")

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
