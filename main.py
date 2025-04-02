import pygame
from constants import *
from player import *
def main():
    pygame.init()
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    Player.containers = (drawables, updatables)
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        screen.fill("black")
        drawables.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
