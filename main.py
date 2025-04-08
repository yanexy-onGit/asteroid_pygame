import constants as C
import pygame as pg
from player import Player
from asteroid import Asteroid
from bullet import Bullet
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    drawable, updatable, asteroids, bullets = pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    Bullet.containers = (drawable, updatable, bullets)
    player = Player(C.SCREEN_WIDTH / 2, C.SCREEN_HEIGHT / 2)
    AsteroidField()
    clock = pg.time.Clock()
    dt = 0
    while True:
        screen.fill("#000000")

        for e in pg.event.get():
            if e.type == pg.QUIT:
                return

        updatable.update(dt)
        for aster in asteroids:
            if player.is_colliding(aster):
                print("Game over!")
                return
            for shot in bullets:
                if shot.is_colliding(aster):
                    aster.take_hit()
                    shot.kill()
        for member in drawable:
            member.draw(screen)
        
        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()