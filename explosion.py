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

        test = self.explosion_shape()
        print(int(self.position.x), int(self.position.y))
        for vector in test:
            print(f'{int(vector.x), int(vector.y)}', end=", ")

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

        # for x in range(0, 5):
        #     points.append(points[x].rotate(90))
        # for x in range(5, 10):
        #     points.append(points[x].rotate(180))
        # for x in range(10, 15):
        #     points.append(points[x].rotate(270))
        return points
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.explosion_shape(), 2)

    def update(self, dt):
        self.radius -= 1
        if self.radius <= 0:
            self.kill()

    def collides_with_circle(self, circle):
        if self.position.distance_to(circle.position) < self.radius + circle.radius:
            return True
        return False