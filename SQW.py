import pygame as pg
import Action
import Map
pg.init()
point = 80


def run_execution_list():
    for choice in Action.execution_list:
        if choice == "go_straight":
            if Action.status[0] == "R":
                Map.current_x += 80
                Action.moving_arrow_r(Map.current_x, Map.current_y)
            if Action.status[0] == "L":
                Map.current_x -= 80
                Action.moving_arrow_l(Map.current_x, Map.current_y)
            if Action.status[0] == "D":
                Map.current_y += 80
                Action.moving_arrow_d(Map.current_x, Map.current_y)
            if Action.status[0] == "U":
                Map.current_y -= 80
                Action.moving_arrow_u(Map.current_x, Map.current_y)
        if choice == "turn_left":
            if Action.status[0] == "R":
                Action.moving_arrow_u(Map.current_x, Map.current_y)  # In this case, the status changes to "L" when the "turn left" button is pressed.
            if Action.status[0] == "L":
                Action.moving_arrow_d(Map.current_x, Map.current_y)  # In this case, the status changes to "R" when the "turn left" button is pressed.
            if Action.status[0] == "D":
                Action.moving_arrow_r(Map.current_x, Map.current_y)
            if Action.status[0] == "U":
                Action.moving_arrow_l(Map.current_x, Map.current_y)
        if choice == "turn_right":
            if Action.status[0] == "R":
                Action.moving_arrow_d(Map.current_x, Map.current_y)  # In this case, the status changes to "L" when the "turn right" button is pressed.
            if Action.status[0] == "L":
                Action.moving_arrow_u(Map.current_x, Map.current_y)  # In this case, the status changes to "R" when the "turn right" button is pressed.
            if Action.status[0] == "D":
                Action.moving_arrow_l(Map.current_x, Map.current_y)
            if Action.status[0] == "U":
                Action.moving_arrow_r(Map.current_x, Map.current_y)


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
        Map.ourScreen.blit(Map.arrow_r, (Map.current_x, Map.current_y))
        pg.draw.rect(Map.ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    __main__()

