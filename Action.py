import pygame as pg
import Map
import SQW
pg.init()


execution_list = []
status = ["U"]


def turn_right_r():
    rotated = pg.transform.rotate(Map.arrow_r, -90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("D")


def turn_left_r():
    rotated = pg.transform.rotate(Map.arrow_r, 90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("U")


def turn_right_l():
    rotated = pg.transform.rotate(Map.arrow_l, -90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("U")


def turn_left_l():
    rotated = pg.transform.rotate(Map.arrow_l, 90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("D")


def turn_right_d():
    rotated = pg.transform.rotate(Map.arrow_d, -90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("L")


def turn_left_d():
    rotated = pg.transform.rotate(Map.arrow_d, 90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("R")


def turn_right_u():
    rotated = pg.transform.rotate(Map.arrow_u, -90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("R")


def turn_left_u():
    rotated = pg.transform.rotate(Map.arrow_u, 90)
    rect = rotated.get_rect()
    rect.center = (Map.current_x + 40, Map.current_y + 40)
    Map.ourScreen.blit(rotated, rect)
    status.pop()
    status.append("L")


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


def quit(x, y):
    Map.ourScreen.blit(Map.quit, (x, y))


def option(x, y):
    Map.ourScreen.blit(Map.option, (x, y))


