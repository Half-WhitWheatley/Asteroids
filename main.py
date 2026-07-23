import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from insults import get_insult
import sys
import os

def main():
    pygame.init()
    pygame.font.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score: int = 0
    while True:
        log_state()
        font = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print(f"Your score: {score}")
                print(get_insult())
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()
                    score += a.radius // 2
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
