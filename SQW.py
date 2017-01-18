import pygame as pg
import SQW_Action
import SQW_Map
pg.init()
point = 80


def run_TT():
    if SQW_Action.Action.status[0] == 1:
        for choice in SQW_Action.Action.TT:
            if choice == "1":
                SQW_Action.Action.moving_arrow_r(100, 25)  # 좌표가 문제
                print(type(choice))
            elif choice == "2":
                SQW_Action.Action.moving_arrow_u(20, 25)
            elif choice == "3":
                SQW_Action.Action.moving_arrow_d(20, 25)
            else:
                pass


def __main__():
    clock = pg.time.Clock()
    finished = False
    while not finished:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finished = True
            if event.type == pg.MOUSEBUTTONDOWN:
                for x in range(555, 615):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("go straight")
                            SQW_Action.Action.TT.append("1")
                for x in range(630, 690):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn left")
                            SQW_Action.Action.TT.append(2)
                for x in range(705, 765):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn right")
                            SQW_Action.Action.TT.append(3)
                for x in range(555, 615):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("action")
                            SQW_Action.Action.TT.append(4)
                for x in range(630, 690):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("clear")
                for x in range(705, 765):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("run")
                for x in range(555, 655):
                    for y in range(180, 200):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("option")
                for x in range(665, 765):
                    for y in range(180, 200):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("setting")
        SQW_Map.Map.ourScreen.fill((0, 0, 0))
        SQW_Map.Map.ourScreen.blit(SQW_Map.Map.map, (20, 20))
        pg.draw.rect(SQW_Map.Map.ourScreen, (0, 255, 0), pg.Rect(540, 20, 240, 190))  # button part
        SQW_Action.Action.moving_arrow_r(20, 25)
        SQW_Action.Action.straight(555, 35)
        SQW_Action.Action.left(630, 35)
        SQW_Action.Action.right(705, 35)
        SQW_Action.Action.action(555, 110)
        SQW_Action.Action.clear(630, 110)
        SQW_Action.Action.run(705, 110)
        SQW_Action.Action.option(555, 180)
        SQW_Action.Action.setting(665, 180)
        SQW_Action.Action.moving_arrow_r(SQW_Map.Map.a, SQW_Map.Map.b)
        pg.draw.rect(SQW_Map.Map.ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    __main__()

