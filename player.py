import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.x = int(x)
        self.y = int(y)
        self.rotation = 0
        self.timer = 0
        self.velocity = pygame.Vector2(0, 0)
        self.angularMomentum = 0
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
            self.boost(dt)  # Apply forward thrust
            
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Apply velocity to position
        self.position += self.velocity * dt

        # Apply friction
        self.velocity *= PLAYER_FRICTION  # Gradually reduce velocity
        if self.velocity.length() < 0.1:  # Stop micro-movements
            self.velocity = pygame.Vector2(0, 0)

        self.timer -= dt

    def boost(self, dt):
        # Increase velocity in the direction the player is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_THRUST * dt  # PLAYER_THRUST determines the acceleration

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        # Calculate the position of the shot at the front of the ship
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction the player is facing
        shot = Shot(self.position.x + forward.x * OUTER_PLAYER_RADIUS, self.position.y + forward.y * OUTER_PLAYER_RADIUS, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
