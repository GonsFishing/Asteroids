import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def explosion_shape(self):
        up = pygame.Vector2(0, 1)
        right = pygame.Vector2(1, 0)
        #top right shape

        points = []
        base_points = []
        base_points.append(up * self.radius)
        base_points.append((up * 0.5) * self.radius + (right * 0.2) * self.radius)
        base_points.append((up * 0.8) * self.radius + (right * 0.8) * self.radius)
        base_points.append((up * 0.2) * self.radius + (right * 0.5) * self.radius)
        base_points.append(right * self.radius)

        #the other 3 directions
        for point in base_points:
            points.append(point + self.position)
        
        for x in [-90, -180, -270]:
            for point in base_points:
                points.append(point.rotate(x) + self.position)
        return points
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.explosion_shape(), 2)

    def update(self, dt):
        self.radius -= 100 * dt
        if self.radius <= 0:
            self.kill()

    def collides_with_circle(self, circle):
        if self.position.distance_to(circle.position) < self.radius + circle.radius:
            return True
        return False