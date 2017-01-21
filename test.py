import Action
import Map


def run_execution_list():
    for choice in Action.execution_list:
        if choice == 1:
            if Action.status[0] == 1:
                Action.moving_arrow_r(Map.current_x + 80, Map.current_y)
            if Action.status[0] == 2:
                Action.moving_arrow_l(Map.current_x - 80, Map.current_y)
            if Action.status[0] == 3:
                Action.moving_arrow_d(Map.current_x, Map.current_y + 80)
            if Action.status[0] == 4:
                Action.moving_arrow_u(Map.current_x, Map.current_y - 80)
        if choice == 2:
            if Action.status[0] == 1:
                Action.moving_arrow_u(Map.current_x, Map.current_y)
            if Action.status[0] == 2:
                Action.moving_arrow_d(Map.current_x, Map.current_y)
            if Action.status[0] == 3:
                Action.moving_arrow_r(Map.current_x, Map.current_y)
            if Action.status[0] == 4:
                Action.moving_arrow_l(Map.current_x, Map.current_y)
        if choice == 3:
            if Action.status[0] == 1:
                Action.moving_arrow_d(Map.current_x, Map.current_y)
            if Action.status[0] == 2:
                Action.moving_arrow_u(Map.current_x, Map.current_y)
            if Action.status[0] == 3:
                Action.moving_arrow_l(Map.current_x, Map.current_y)
            if Action.status[0] == 4:
                Action.moving_arrow_r(Map.current_x, Map.current_y)