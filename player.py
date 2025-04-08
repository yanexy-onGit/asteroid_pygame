import constants as C
import pygame as pg
from bullet import Bullet
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, C.PLAYER_RADIUS)
        self.__rotation = 180
        self.__shoot_keys_were_released = True
        self.__gun_cooldown = 0
        self.__uptime = 0 # for testing
    def __has_enough_up(self, ticks=600): # for testing
        self.__uptime += 1
        if self.__uptime >= ticks:
            self.__uptime %= ticks
            return True
        return False
    def __triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.__rotation)
        right = pg.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pg.draw.polygon(screen, C.CLR_PLAYER, self.__triangle(), C.DRAW_LINE_WIDTH)
    def __rotate(self, dt):
        self.__rotation += (C.PLAYER_TURN_SPEED * dt)
        self.__rotation %= 360
    def __move(self, dt):
        self.position += pg.Vector2(0, 1).rotate(self.__rotation) * C.PLAYER_SPEED * dt
    def __shoot(self):
        Bullet(*self.position).velocity = pg.Vector2(0, 1).rotate(self.__rotation) * C.BULLET_SPEED
        self.__gun_cooldown = C.PLAYER_GUN_COOLDOWN


    def update(self, dt):
        self.__gun_cooldown -= dt
        keys = pg.key.get_pressed() # iterable of booleans of pressed keys
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.__move(dt)
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.__move(-dt)
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.__rotate(-dt)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.__rotate(dt)
        shoot_key_pressed = keys[pg.K_SPACE] or keys[pg.K_LCTRL] or keys[pg.K_RCTRL]
        if shoot_key_pressed:
            if self.__shoot_keys_were_released or self.__gun_cooldown <= 0:
                self.__shoot()
                self.__shoot_keys_were_released = False
        elif not self.__shoot_keys_were_released:
            self.__shoot_keys_were_released = True