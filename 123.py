import Map
import Action
import pygame as pg
pg.init()
# status = ["R", "D", "L", "U"]
# i = 0
# n_status = status[i]
#
# if choice == "turn left":
#     if i < 4:
#         i += 1
#     else:
#         i = 0
#
# elif choice == "turn right":
#     if i > 0:
#         i -= 1
#     else:
#         i = 3
#
# if i == 0:
#
# elif i == 1:
#
# elid

rotated_d = pg.transform.rotate(Map.arrow_d, 90)
rect = rotated_d.get_rect()
rect.center = (Map.current_x, Map.current_y)
Map.ourScreen.blit(rotated_d, rect)



















