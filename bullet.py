import pygame as pg
import constants as C
from circleshape import CircleShape

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, C.BULLET_RADIUS)

    def draw(self, screen):
        pg.draw.circle(screen, C.CLR_PLAYER, self.position, self.radius, C.DRAW_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt