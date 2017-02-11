import pygame as pg
import Action
import Map
from pygame.locals import *
pg.init()
point = 80
degree = 90


def run_execution_list():
    for choice in Action.execution_list:
        if Action.status[0] == "R":
            if choice == "go_straight":  # work properly
                Map.current_x += 80
            if choice == "turn_right":  # does not work at all
                Action.turn_right_r()
            if choice == "turn_left":  # When it works, it turns to "L"
                Action.turn_left_r()
        if Action.status[0] == "D":
            if choice == "go_straight":  # work properly
                Map.current_y += 80
            if choice == "turn_right":  # when it works, it displays "R" unconditionally.
                Action.turn_right_d()
            if choice == "turn_left":   # work properly
                Action.turn_left_d()
        if Action.status[0] == "L":
            if choice == "go_straight":  # work properly
                Map.current_x -= 80
            if choice == "turn_right":  # when it works, it displays "R" unconditionally.
                Action.turn_right_l()
            if choice == "turn_left":  # work properly
                Action.turn_left_l()
        if Action.status[0] == "U":
            if choice == "go_straight":  # work properly
                Map.current_y -= 80
            if choice == "turn_right":  # work properly
                Action.turn_right_u()
            if choice == "turn_left":  # work properly
                Action.turn_left_u()


def __main__():
    clock = pg.time.Clock()
    finished = False
    while not finished:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for x in range(555, 615):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("go straight")
                            Action.execution_list.append("go_straight")
                for x in range(630, 690):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn left")
                            Action.execution_list.append("turn_left")
                for x in range(705, 765):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn right")
                            Action.execution_list.append("turn_right")
                for x in range(555, 615):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("action")
                            Action.execution_list.append("action")
                for x in range(630, 690):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("clear")
                            del Action.execution_list[:]
                for x in range(705, 765):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            run_execution_list()
                            print("run")
                            pg.display.flip()
                for x in range(555, 655):
                    for y in range(180, 200):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("option")
                for x in range(665, 765):
                    for y in range(180, 200):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("Quit")
                            finished = True
        Map.ourScreen.fill((0, 0, 0))
        Map.ourScreen.blit(Map.map1, (20, 25))
        print(Action.status)
        print(Action.execution_list)
        pg.draw.rect(Map.ourScreen, (0, 255, 0), pg.Rect(540, 20, 240, 190))  # button part
        Action.straight(555, 35)
        Action.left(630, 35)
        Action.right(705, 35)
        Action.action(555, 110)
        Action.clear(630, 110)
        Action.run(705, 110)
        Action.option(555, 180)
        Action.quit(665, 180)
        pg.draw.rect(Map.ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        Map.ourScreen.blit(Map.arrow_r, (Map.current_x, Map.current_y))  # this line
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    __main__()

# i don't know how to fix the method run_execution_list
