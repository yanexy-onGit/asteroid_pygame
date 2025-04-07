import constants as C
import pygame as pg

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    while True:
        screen.fill("#000000")

        for e in pg.event.get():
            if e.type == pg.QUIT:
                return


        pg.display.flip()

if __name__ == "__main__":
    main()