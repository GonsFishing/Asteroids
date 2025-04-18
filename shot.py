import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
class Shot(CircleShape):
    def __init__(self, x, y, speed, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * speed

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt


