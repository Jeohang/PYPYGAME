import pygame as pg
import time
import Action
import Map
pg.init()
i = 0
j = 2
point = 80


def run_execution_list():
    global i, j
    for choice in Action.execution_list:
        if choice == "go_straight":
            if Action.status_list[i] == "R":
                Map.current_x += 80
            elif Action.status_list[i] == "D":
                Map.current_y += 80
            elif Action.status_list[i] == "L":
                Map.current_x -= 80
            elif Action.status_list[i] == "U":
                Map.current_y -= 80
        elif choice == "turn_right":
            rotated = pg.transform.rotate(Map.arrow_r, -90)
            rect = rotated.get_rect()
            rect.center = (Map.current_x + 40, Map.current_y + 40)
            Map.ourScreen.blit(rotated, rect)
            if i < 3:
                i += 1
            elif i == 3:
                i = 0
        elif choice == "turn_left":
            rotated = pg.transform.rotate(Map.arrow_r, 90)
            rect = rotated.get_rect()
            rect.center = (Map.current_x + 40, Map.current_y + 40)
            Map.ourScreen.blit(rotated, rect)
            if i > 0:
                i -= 1
            elif i == 0:
                i = 3
        elif choice == "action":
            if j == 0:
                if Map.current_x == 420 and Map.current_y == 345:
                    print("Clear!")
                    j += 1
                    i = 0
                    Map.current_x = 20
                    Map.current_y = 25
            if j == 1:
                if Map.current_x == 20 and Map.current_y == 185:
                    Map.current_y += 160
                elif Map.current_x == 260 and Map.current_y == 25:
                    Map.current_x += 160
                elif Map.current_x == 420 and Map.current_y == 345:
                    print("Clear!")
                    j += 1
                    i = 0
                    Map.current_x = 20
                    Map.current_y = 25
            elif j == 2:
                if Map.current_x == 100 and Map.current_y == 345:
                    Map.current_x = 340
                    Map.current_y = 25
                elif Map.current_x == 180 and Map.current_y == 105:
                    Map.current_x = 420
                    Map.current_y = 105
                elif Map.current_x == 340 and Map.current_y == 345:
                    print("Clear!")


def __main__():
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
        Map.ourScreen.blit(Map.map_list[j], (20, 25))
        print(Action.status_list[i])
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
        Map.ourScreen.blit(Action.arrow_status[i], (Map.current_x, Map.current_y))  # this line
        pg.display.flip()


if __name__ == '__main__':
    __main__()
