import pygame as pg
pg.init()
point = 80


class Map:
    display_width = 800
    display_height = 450
    ourScreen = pg.display.set_mode((display_width, display_height))
    rect_x = 80
    rect_y = 80
    arrow = pg.image.load("arrow.jpg")
    a = 20
    b = 25

    def __init__(self):
        pass


class Action:
    mouse_pos = pg.mouse.get_pos()

    def __init__(self):
        pass

    def moving_arrow(x, y):
        Map.ourScreen.blit(Map.arrow, (x, y))


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
                for x in range(630, 690):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn left")
                for x in range(705, 765):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn right")
                for x in range(555, 615):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("action")
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
        Map.ourScreen.fill((0, 0, 0))
        Action.moving_arrow(Map.a, Map.b)
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]: Map.b -= 5
        if pressed[pg.K_DOWN]: Map.b += 5
        if pressed[pg.K_RIGHT]: Map.a += 5
        if pressed[pg.K_LEFT]: Map.a -= 5
        # pg.draw.rect(Map.ourScreen, (255, 255, 255), pg.Rect(20, 20, 500, 410))  # running part
        pg.draw.rect(Map.ourScreen, (0, 255, 0), pg.Rect(540, 20, 240, 190))  # button part
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(555, 35, 60, 55))  # 555, 35, 60, 55
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(630, 35, 60, 55))  # 630, 35, 60, 55
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(705, 35, 60, 55))  # 705, 35, 60, 55
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(555, 110, 60, 55))  # 555, 110, 60, 55
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(630, 110, 60, 55))  # 630, 110, 60, 55
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(705, 110, 60, 55))   # 705, 110, 60, 55
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(555, 180, 100, 20))  # 555, 180, 100, 20
        pg.draw.rect(Map.ourScreen, (155, 155, 155), pg.Rect(665, 180, 100, 20))  # 665, 180, 100, 20
        pg.draw.rect(Map.ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    __main__()

