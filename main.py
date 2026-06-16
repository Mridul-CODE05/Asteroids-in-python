from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *
import pygame, sys



def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        updatable.update(dt)   
        for aste_roid in asteroids:
            for shot in shots:
                if aste_roid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    aste_roid.kill()
            if aste_roid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()  
        screen.fill("black")
        for draw_able in drawable:
            draw_able.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
