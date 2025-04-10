import sys, pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from explosion import Explosion
from ui_helper import draw_text
from scoring import set_score

def main():
    pygame.init()
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, drawables, updatables)
    Explosion.containers = (drawables, updatables)



    AsteroidField()
    score = 0
    dt = 0
    font = pygame.font.SysFont("comic sans", 30)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with_circle(player):
                print("Game over!")
                set_score(score)
                sys.exit(0)
            for shot in shots:
                if asteroid.collides_with_circle(shot):
                    score += 1
                    asteroid.split()
                    shot.kill()

        #Draw
        screen.fill("black")
        for object in drawables:
            object.draw(screen)
        draw_text(screen, f'Score: {score}', font, "white", SCREEN_WIDTH - (SCREEN_WIDTH/10), SCREEN_HEIGHT - (SCREEN_HEIGHT/10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
