# coding=utf-8
import pygame as pg
pg.init()


class Map:
    display_width = 800
    display_height = 450

    def __init__(self):
        pass


class Action:
    pass


def __main__():
    clock = pg.time.Clock()
    ourScreen = pg.display.set_mode((map.display_width, map.display_height))
    finished = False
    while not finished:
        ourScreen.fill((0, 0, 0))
        pg.draw.rect(ourScreen, (255, 255, 255), pg.Rect(20, 20, 500, 410))  # running part
        pg.draw.rect(ourScreen, (0, 255, 0), pg.Rect(540, 20, 240, 190))  # button part
        pg.draw.rect(ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        pg.display.flip()
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finished = True


if __name__ == '__main__':
    __main__()







