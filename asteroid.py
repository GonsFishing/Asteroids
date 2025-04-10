import pygame, random
from circleshape import CircleShape
from explosion import Explosion
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_MULTIPLIER

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        Explosion(self.position.x, self.position.y, self.radius)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
            vel2 = self.velocity.rotate(-angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
            Asteroid(self.position.x, self.position.y, radius).velocity = vel1
            Asteroid(self.position.x, self.position.y, radius).velocity = vel2

