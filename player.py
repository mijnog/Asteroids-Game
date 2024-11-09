#player.py
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
class Player(CircleShape):

    def __init__(self, x, y, PLAYER_RADIUS):
        # Pass x, y, and PLAYER_RADIUS to the CircleShape constructor
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.x = int(x)
        self.y = int(y)
        self.rotation = 0
        self.timer = 0
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
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    #ChatGPT please help!
    #Create a new shot at the position of the player
    #Set the shot's velocity:
        #Start with a pygame.Vector2 of (0,1)
        #rotate() in the direction the player is facing
        #scale it up by PLAYER_SHOOT_SPEED to make it move faster
    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        
          # Calculate the position of the shot at the front of the ship
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction the player is facing
        shot = Shot(self.position.x + forward.x * OUTER_PLAYER_RADIUS, self.position.y + forward.y * OUTER_PLAYER_RADIUS, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

