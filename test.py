import Action
import Map


def run_execution_list():
    for choice in Action.execution_list:
        if choice == "go_straight":
            if Action.status[0] == "R":
                Map.current_x += 80
            if Action.status[0] == "U":
                Map.current_y -= 80
            if Action.status[0] == "L":
                Map.current_x -= 80
            if Action.status[0] == "D":
                Map.current_y += 80
        if choice == "turn_left":
            if Action.status[0] == "R":
                Action.turn_left_r()
            if Action.status[0] == "U":
                Action.turn_left_u()
            if Action.status[0] == "L":
                Action.turn_left_l()
            if Action.status[0] == "D":
                Action.turn_left_d()
        if choice == "turn_right":
            if Action.status[0] == "R":
                Action.turn_right_r()
            if Action.status[0] == "U":
                Action.turn_right_u()
            if Action.status[0] == "L":
                Action.turn_right_l()
            if Action.status[0] == "D":
                Action.turn_right_d()
