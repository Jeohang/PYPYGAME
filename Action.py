import pygame as pg
import Map
import SQW
pg.init()


execution_list = []  # 1(s), 2(l), 3(r), 4(a)
status = [0]


def moving_arrow_r(x, y):
    Map.ourScreen.blit(Map.arrow_r, (x, y))
    status.pop()
    status.append(1)


def moving_arrow_l(x, y):
    Map.ourScreen.blit(Map.arrow_l, (x, y))
    status.pop()
    status.append(2)


def moving_arrow_d(x, y):
    Map.ourScreen.blit(Map.arrow_d, (x, y))
    status.pop()
    status.append(3)


def moving_arrow_u(x, y):
    Map.ourScreen.blit(Map.arrow_u, (x, y))
    status.pop()
    status.append(4)


def straight(x, y):
    Map.ourScreen.blit(Map.straight, (x, y))


def left(x, y):
    Map.ourScreen.blit(Map.left, (x, y))


def right(x, y):
    Map.ourScreen.blit(Map.right, (x, y))


def action(x, y):
    Map.ourScreen.blit(Map.action, (x, y))


def clear(x, y):
    Map.ourScreen.blit(Map.clear, (x, y))


def run(x, y):
    Map.ourScreen.blit(Map.run, (x, y))


def setting(x, y):
    Map.ourScreen.blit(Map.setting, (x, y))


def option(x, y):
    Map.ourScreen.blit(Map.option, (x, y))
