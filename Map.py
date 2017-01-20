import pygame as pg
import Action
import SQW
pg.init()

display_width = 800
display_height = 450
ourScreen = pg.display.set_mode((display_width, display_height))
rect_x = 80
rect_y = 80
arrow_r = pg.image.load("arrows\\arrow_r.jpg")
arrow_l = pg.image.load("arrows\\arrow_l.jpg")
arrow_d = pg.image.load("arrows\\arrow_d.jpg")
arrow_u = pg.image.load("arrows\\arrow_u.jpg")
straight = pg.image.load("button\\straight.jpg")
left = pg.image.load("button\\left.jpg")
right = pg.image.load("button\\right.jpg")
action = pg.image.load("button\\action.jpg")
clear = pg.image.load("button\\clear.jpg")
run = pg.image.load("button\\run.jpg")
setting = pg.image.load("button\\setting.jpg")
option = pg.image.load('button\\option.jpg')
map1 = pg.image.load("maps\\map1.jpg")
a = 20
b = 25
current_x = 20
current_y = 25
