import pygame as pg
import SQW_Map
import SQW
pg.init()


class Action:
    TT = []  # 1(s), 2(l), 3(r), 4(a)
    status = [0]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moving_arrow_r(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.arrow_r, (x, y))
        Action.status.pop()
        Action.status.append(1)

    def moving_arrow_l(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.arrow_l, (x, y))
        Action.status.pop()
        Action.status.append(2)

    def moving_arrow_d(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.arrow_d, (x, y))
        Action.status.pop()
        Action.status.append(3)

    def moving_arrow_u(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.arrow_u, (x, y))
        Action.status.pop()
        Action.status.append(4)

    def straight(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.straight, (x, y))

    def left(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.left, (x, y))

    def right(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.right, (x, y))

    def action(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.action, (x, y))

    def clear(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.clear, (x, y))

    def run(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.run, (x, y))

    def setting(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.setting, (x, y))

    def option(x, y):
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.option, (x, y))