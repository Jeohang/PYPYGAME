import pygame as pg
import Map
import SQW
pg.init()


execution_list = []
status_list = ["R", "D", "L", "U"]


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


