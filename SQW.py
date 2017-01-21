import pygame as pg
import Action
import Map
pg.init()
point = 80


def run_execution_list():
    if Action.status[0] == 1:
        for choice in Action.execution_list:
            if choice == 1:
                Action.moving_arrow_r(Map.current_x + 80, Map.current_y)
            elif choice == 2:
                Action.moving_arrow_u(Map.current_x, Map.current_y)
            elif choice == 3:
                Action.moving_arrow_d(Map.current_x, Map.current_y)
    if Action.status[0] == 2:
        for choice in Action.execution_list:
            if choice == 1:
                Action.moving_arrow_l(Map.current_x - 80, Map.current_y)
            if choice == 2:
                Action.moving_arrow_d(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_u(Map.current_x, Map.current_y)
    if Action.status[0] == 3:
        for choice in Action.execution_list:
            if choice == 1:
                Action.moving_arrow_d(Map.current_x, Map.current_y + 80)
            if choice == 2:
                Action.moving_arrow_r(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_l(Map.current_x, Map.current_y)
    if Action.status[0] == 4:
        for choice in Action.execution_list:
            if choice == 1:
                Action.moving_arrow_u(Map.current_x, Map.current_y - 80)
            if choice == 2:
                Action.moving_arrow_l(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_r(Map.current_x, Map.current_y)


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
                            Action.execution_list.append(1)
                for x in range(630, 690):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn left")
                            Action.execution_list.append(2)
                for x in range(705, 765):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn right")
                            Action.execution_list.append(3)
                for x in range(555, 615):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("action")
                            Action.execution_list.append(4)
                for x in range(630, 690):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("clear")
                for x in range(705, 765):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            run_execution_list()
                            print("run")
                for x in range(555, 655):
                    for y in range(180, 200):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("option")
                for x in range(665, 765):
                    for y in range(180, 200):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("setting")
        Map.ourScreen.fill((0, 0, 0))
        Map.ourScreen.blit(Map.map1, (20, 20))
        print(Action.status)
        pg.draw.rect(Map.ourScreen, (0, 255, 0), pg.Rect(540, 20, 240, 190))  # button part
        Action.straight(555, 35)
        Action.left(630, 35)
        Action.right(705, 35)
        Action.action(555, 110)
        Action.clear(630, 110)
        Action.run(705, 110)
        Action.option(555, 180)
        Action.setting(665, 180)
        Map.ourScreen.blit(Map.arrow_r, (Map.current_x, Map.current_y))
        pg.draw.rect(Map.ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    __main__()

