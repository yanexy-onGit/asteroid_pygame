from random import uniform as ran_float_in_range
import pygame as pg
import constants as C
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, rad):
        super().__init__(x, y, rad)
    
    def draw(self, screen):
        pg.draw.circle(screen, C.CLR_ENEMY, self.position, self.radius, C.DRAW_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def take_hit(self):
        self.kill()
        if self.radius <= C.ASTEROID_MIN_RADIUS:
            return
        split_angle = ran_float_in_range(20, 50)
        self.velocity *= 1.2
        vector_a = self.velocity.rotate(split_angle)
        vector_b = self.velocity.rotate(-split_angle)
        Asteroid(*self.position, self.radius - C.ASTEROID_MIN_RADIUS).velocity = vector_a        
        Asteroid(*self.position, self.radius - C.ASTEROID_MIN_RADIUS).velocity = vector_b