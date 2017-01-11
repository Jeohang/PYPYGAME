# coding=utf-8
import pygame as pg
pg.init()
display_width = 1000
display_height = 1000

ourScreen = pg.display.set_mode((display_width, display_height))

myImg = pg.image.load('20160815.jpg')
def myimg(x, y):
    ourScreen.blit(myImg,(x,y))

x = (display_width * 0.5)
y = (display_height * 0.5)

finished = False
while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    ourScreen.fill((255,255,255))
    myimg(x,y)
    pg.display.flip()
pg.quit()
quit()