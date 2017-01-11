# coding=utf-8
import pygame as pg

pg.init()

ourScreen = pg.display.set_mode((800, 450))  # display size
pg.display.set_caption("layout view")
finish = False

clock = pg.time.Clock()
while not finish:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
    ourScreen.fill((0, 0, 0))

    pg.draw.rect(ourScreen, (0, 155, 156), pg.Rect(20, 20, 500, 410))  # display
    pg.draw.rect(ourScreen, (200, 155, 0), pg.Rect(540, 20, 240, 190))  # button
    pg.draw.rect(ourScreen, (155, 155, 155), pg.Rect(540, 230, 240, 200))

    pg.display.flip()
    clock.tick(60)
