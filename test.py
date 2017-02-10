import Action
import Map

# Test code does not work at all.


def run_execution_list():
    if Action.status[0] == "R":
        for choice in Action.execution_list:
            if choice == 1:
                Map.current_x += 80
                Action.moving_arrow_r(Map.current_x, Map.current_y)
            if choice == 2:
                Action.moving_arrow_u(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_d(Map.current_x, Map.current_y)
    if Action.status[0] == "L":
        for choice in Action.execution_list:
            if choice == 1:
                Map.current_x -= 80
                Action.moving_arrow_l(Map.current_x, Map.current_y)
            if choice == 2:
                Action.moving_arrow_d(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_u(Map.current_x, Map.current_y)
    if Action.status[0] == "D":
        for choice in Action.execution_list:
            if choice == 1:
                Map.current_y += 80
                Action.moving_arrow_d(Map.current_x, Map.current_y)
            if choice == 2:
                Action.moving_arrow_r(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_l(Map.current_x, Map.current_y)
    if Action.status[0] == "U":
        for choice in Action.execution_list:
            if choice == 1:
                Map.current_y -= 80
                Action.moving_arrow_u(Map.current_x, Map.current_y)
            if choice == 2:
                Action.moving_arrow_l(Map.current_x, Map.current_y)
            if choice == 3:
                Action.moving_arrow_r(Map.current_x, Map.current_y)


rotated = pygame.transform.rotate(img, degree)
rect = rotated.get_rect()
rect.center = (x, y)
screen.blit(rotated, rect)