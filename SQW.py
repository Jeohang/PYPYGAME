import pygame as pg
pg.init()
point = 80


class Map:
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
    option = pg.image.load("button\\option.jpg")
    map = pg.image.load("maps\\map1.jpg")
    a = 20
    b = 25

    def __init__(self):
        pass


class Action:
    TT = []  # 1(s), 2(l), 3(r), 4(a)

    def __init__(self):
        pass

    def moving_arrow_r(x, y):
        Map.ourScreen.blit(Map.arrow_r, (x, y))

    def moving_arrow_l(x, y):
        Map.ourScreen.blit(Map.arrow_l, (x, y))

    def moving_arrow_d(x, y):
        Map.ourScreen.blit(Map.arrow_d, (x, y))

    def moving_arrow_u(x, y):
        Map.ourScreen.blit(Map.arrow_u, (x, y))

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
                            Action.TT.append(1)
                for x in range(630, 690):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn left")
                            Action.TT.append(2)
                for x in range(705, 765):
                    for y in range(35, 90):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("turn right")
                            Action.TT.append(3)
                for x in range(555, 615):
                    for y in range(110, 165):
                        if (event.pos[0], event.pos[1]) == (x, y):
                            print("action")
                            Action.TT.append(4)
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
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            Map.b -= 5
        if pressed[pg.K_DOWN]:
            Map.b += 5
        if pressed[pg.K_RIGHT]:
            Map.a += 5
        if pressed[pg.K_LEFT]:
            Map.a -= 5
        #  pg.draw.rect(Map.ourScreen, (255, 255, 255), pg.Rect(20, 20, 500, 410))  # running part
        Map.ourScreen.blit(Map.map, (20, 20))
        pg.draw.rect(Map.ourScreen, (0, 255, 0), pg.Rect(540, 20, 240, 190))  # button part
        Action.straight(555, 35)
        Action.left(630, 35)
        Action.right(705, 35)
        Action.action(555, 110)
        Action.clear(630, 110)
        Action.run(705, 110)
        Action.option(555, 180)
        Action.setting(665, 180)
        Action.moving_arrow_r(Map.a, Map.b)
        pg.draw.rect(Map.ourScreen, (0, 255, 255), pg.Rect(540, 230, 240, 200))  # function part
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    __main__()

