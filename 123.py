import Map
import Action
import pygame as pg
pg.init()


def run_execution_list():
    for choice in Action.execution_list:
        if Action.status[0] == "R":
            if choice == "go_straight":
                Map.current_x += 80
            if choice == "turn_right":
                Action.turn_right_r()
            if choice == "turn_left":
                Action.turn_left_r()
        if Action.status[0] == "D":
            if choice == "go_straight":
                Map.current_y += 80
            if choice == "turn_right":
                Action.turn_right_d()
            if choice == "turn_left":
                Action.turn_left_d()
        if Action.status[0] == "L":
            if choice == "go_straight":
                Map.current_x -= 80
            if choice == "turn_right":
                Action.turn_right_l()
            if choice == "turn_left":
                Action.turn_left_l()
        if Action.status[0] == "U":
            if choice == "go_straight":
                Map.current_y -= 80
            if choice == "turn_right":
                Action.turn_right_u()
            if choice == "turn_left":
                Action.turn_left_u()

















